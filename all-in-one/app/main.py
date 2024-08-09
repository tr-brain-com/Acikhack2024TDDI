import transformers
from fastapi import FastAPI
from pydantic import BaseModel, Field
from spacy.tokens import Doc
import uvicorn
import spacy
import os
import re
import torch
import numpy as np
import pandas as pd
import json
import pickle
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline, AutoModelForTokenClassification
import logging

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S', level=logging.INFO)
app = FastAPI(title="BRAIN-TR NLP")

tags = ['APP', 'OPERATOR', 'PRODUCT', 'HIZMET', 'O', 'PACKAGE', 'PAD']

sentimentPipeline = None
spacyNlp = None

objectpath = "app/models/segmentation/mukayese_punkt_clean.pkl"
sentence_tokenizer =  pickle.load(open(objectpath, "rb"))


def getSpacyModel():
    return spacy.load('tr_core_news_trf')

sentdict = {
    "LABEL_0": "nötr",
    "LABEL_1": "olumlu",
    "LABEL_2": "olumsuz"
}


class Item(BaseModel):
    text: str = Field(...,
                      example="""Fiber 100mb SuperOnline kullanıcısıyım yaklaşık 2 haftadır @Twitch @Kick_Turkey gibi canlı yayın platformlarında 360p yayın izlerken donmalar yaşıyoruz.  Başka hiç bir operatörler bu sorunu yaşamazken ben parasını verip alamadığım hizmeti neden ödeyeyim ? @Turkcell """)


def getSentimentPipeline():
    tokenizer = AutoTokenizer.from_pretrained("app/models/sentimentv2", local_files_only=True)
    model = AutoModelForSequenceClassification.from_pretrained("app/models/sentimentv2", local_files_only=True)
    sentiment_pipeline = pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)
    return sentiment_pipeline

class WhitespaceTokenizer:
    def __init__(self, vocab):
        self.vocab = vocab

    def __call__(self, text):
        words = text.split(" ")
        spaces = [True] * len(words)
        # Avoid zero-length tokens
        for i, word in enumerate(words):
            if word == "":
                words[i] = " "
                spaces[i] = False
        # Remove the final trailing space
        if words[-1] == " ":
            words = words[0:-1]
            spaces = spaces[0:-1]
        else:
           spaces[-1] = False

        return Doc(self.vocab, words=words, spaces=spaces)

def getNerResponse(sentence):
    model_path = "app/models/ner"
    tokenizer = AutoTokenizer.from_pretrained(model_path, do_lower_case=False, local_files_only=True)
    model = AutoModelForTokenClassification.from_pretrained(
        model_path
    )
    tokenized_sentence = tokenizer.encode(sentence)
    input_ids = torch.tensor([tokenized_sentence])

    with torch.no_grad():
        output = model(input_ids)
    label_indices = np.argmax(output[0].to("cpu").numpy(), axis=2)

    tokens = tokenizer.convert_ids_to_tokens(input_ids.to('cpu').numpy()[0])
    new_tokens, new_labels = [], []
    for token, label_idx in zip(tokens, label_indices[0]):
        if token.startswith("##"):
            new_tokens[-1] = new_tokens[-1] + token[2:]
        else:
            new_labels.append(tags[label_idx])
            new_tokens.append(token)

    import json

    process_tag = ['OPERATOR', 'PRODUCT', 'HIZMET', 'APP', 'PACKAGE']
    custom_tags = ["[CLS]", "[SEP]"]
    outputs = []
    entity_index = 0
    for indx, (token, label) in enumerate(zip(new_tokens, new_labels)):
        if not token in custom_tags:
            if label in process_tag:
                if new_labels[indx - 1] in process_tag:
                    entity_index = entity_index
                else:
                    entity_index += 1

                outputs.append(
                    {"entitiy": "OTHER" if label in ["PAD", "O"] else label, "word": token, "entityindex": entity_index,
                     "wordindex": indx - 1})
            else:

                outputs.append(
                    {"entitiy": "OTHER" if label in ["PAD", "O"] else label, "word": token, "entityindex": -1,
                     "wordindex": indx - 1})
            # if new_labels[index+1] in process_tag:
            # if label in process_tag:

    # print(outputs)
    return outputs

def special_character_clean(text):
    return re.sub(r'["\-;%()|&+=^*%.”“’,!?¦‘:#$@\[\]/<>]', '', text)


def cleanSpaces(rawText):
    #return str(rawText).replace("\'", "").replace('"', "").replace("\t", "").replace("\n", "")
    rawText = re.sub(('\s+'), ' ', rawText).replace("'", " ").replace('"', " ")

    cleaned = []
    for word in rawText.split():
        if word not in ('in', 'ın', 'un', 'ün', 'nin', 'nın',
                        'nun', 'nün', 'inin', 'ının', 'unun', 'ünün','den','dan',
                        'de','da','ile','le') and len(word)>1:
            cleaned.append(word)
    rawText = ' '.join(cleaned)
    rawText = special_character_clean(rawText)

    return rawText


def splitSentencesByDependecies(data):

    sentences = dict()
    sentence = ""
    entities = []
    sentence_hold = ""

    if len(data[data['entityindex'] > 0]['entityindex'].unique().tolist()) > 1:
        for index, row in data.iterrows():
            if row["pos_"] != 'PUNCT':
                sentence += row["token"] + " "
            if row["entitiy"] != 'OTHER':
                if len(row["token"]) > 1:
                    entities.append([row["token"], row["entityindex"]])
            print(row['token'], row['pos_'], row['dep_'])
            if (((row["pos_"] == 'VERB') and row["dep_"] not in ('nsubj', 'xcomp', 'acl', 'dep')) or
                    #(row["pos_"] == 'NOUN' and row["dep_"] in ('advcl', 'ROOT')) or
                    (row["pos_"] == 'NOUN' and row["dep_"] in ('advcl')) or
                    (row["pos_"] == 'AUX' and row["dep_"] in ('aux')) or
                    (row["pos_"] == 'CCONJ') and ('cc' in row["dep_"])):
                if len(entities) > 0:
                    sentences[sentence] = entities
                    entities = []
                    sentence_hold = sentence
                    sentence = ""
        if sentence != "" and len(entities) > 0:
            if 'VERB' not in entities:
                sentences[sentence] = entities
        if len(entities) > 0:
            if sentence == "" and sentence_hold != "":
                sentences[sentence_hold] = entities

    else:
        print(f'TEK ENTITY GELDİ!!!!!')
        sentence = ""
        entities = []
        for index, row in data.iterrows():
            if row["entitiy"] != 'OTHER':
                if len(row["token"]) > 1:
                    entities.append([row["token"], row["entityindex"]])
            sentence += row["token"] + " "
        sentences[sentence] = entities

    return sentences


def getSentencesWithIndices(text):

    text_sentences = sentence_tokenizer.tokenize(text)
    print(text_sentences)

    indices = []
    start_index = 0
    end_index = 0
    for sentence in text_sentences:
        end_index = start_index + len(sentence.split(' ')) - 1
        indices.append([start_index, end_index])
        start_index = end_index + 1
    print(indices)

    return text_sentences, indices


def outDependencyForm(doc, start_idx):
    words_dict = dict()
    row_list = []
    for token in doc:
        ancestors = [t.text for t in token.ancestors]
        children = [t.text for t in token.children]
        row_list.append(
            [(start_idx + token.i), token.text, token.lemma_, token.pos_, token.dep_, token.tag_, ancestors, children])
    df_dependency = pd.DataFrame(row_list, columns=['wordindex', 'token', 'lemma_', 'pos_', 'dep_', 'tag_', 'ancestors',
                                                    'children'])
    df_dependency.reset_index(drop=True, inplace=True)

    return df_dependency


def makeResult(out_sentences):
    global sentimentPipeline
    outputs = dict()
    results = []
    entities = []
    for sentences in out_sentences:
        for key, values in sentences.items():
            print(f'sentence : {key}')
            # call sentiment pipeline
            p = sentimentPipeline(key)
            print(p)
            print(f'values are : {values}')
            df_values = pd.DataFrame(values, columns=["text", "index"])
            print(df_values)
            unique_values = df_values["index"].unique()
            print(unique_values)

            for value in unique_values:
                asvalue = ' '.join(df_values[df_values['index'] == value].text.tolist())
                print(asvalue)
                entities.append(asvalue)

                result = dict()
                result['entity'] = asvalue
                label = sentdict[p[0]['label']]

                result['sentiment'] = label
                results.append(result)

    # print(f'..................')
    # print(results)
    # print(sentences.values())

    # outputs['entity_list'] = list(sum([sublist for sublist in sentences.values()], []))
    outputs['entity_list'] = list(entities)
    outputs['results'] = list(np.reshape(list(results), -1))
    # print(outputs['entity_list'])

    return json.dumps(outputs, indent=4, ensure_ascii=False)


def getExcludeTokens(doc):
    print(f'..........Spacy Entites...............')
    exclude_entities = ['LOC', 'GPE', 'PERSON']
    exclude_tokens = []
    for token in doc.ents:
        print(token.label_, token.ents, token.start_char, token.end_char)
        if token.label_ in exclude_entities:
            if ' ' in str(token.ents[0]):
                for ent0 in str(token.ents[0]).split():
                    exclude_tokens.append(str(ent0))
            else:
                exclude_tokens.append(str(token.ents[0]))
    print(exclude_tokens)

    return exclude_tokens


@app.on_event("startup")
def startup_event():
    try:
        global spacyNlp
        global sentimentPipeline
        spacyNlp = getSpacyModel()
        sentimentPipeline = getSentimentPipeline()
    except Exception as e:
        logging.error(f"Model not loaded! Error : {e}")
    logging.info("Server Running Worker PidID : {0}".format(os.getpid()))


@app.on_event("shutdown")
def shutdown_event():
    logging.info("Server Shutdown PidID : {0}".format(os.getpid()))


@app.post("/predict/", response_model=dict)
async def predict(item: Item):
    # Buraya model'in çıktısı gelecek
    # Çıktı formatı aşağıdaki örnek gibi olacak

    #Append each request
    with open('outputs/requests.txt', 'a+') as f:
        f.write(item.text + '\n')

    # Call the entity service
    inputtext = cleanSpaces(item.text)
    nerResponse = getNerResponse(inputtext)
    print(f'........................... {nerResponse}')
    # nerResponse = [{"entitiy": "PRODUCT", "word": "Türk", "entityindex": 1, "wordindex": 0}, {"entitiy": "OPERATOR", "word": "Telekom", "entityindex": 1, "wordindex": 1}, {"entitiy": "OTHER", "word": "tanıdığım", "entityindex": -1, "wordindex": 2}, {"entitiy": "OTHER", "word": "en", "entityindex": -1, "wordindex": 3}, {"entitiy": "OTHER", "word": "iyi", "entityindex": -1, "wordindex": 4}, {"entitiy": "OTHER", "word": "operatörlerden", "entityindex": -1, "wordindex": 5}, {"entitiy": "OTHER", "word": "bir", "entityindex": -1, "wordindex": 6}, {"entitiy": "OTHER", "word": "tanesidir", "entityindex": -1, "wordindex": 7}, {"entitiy": "OTHER", "word": ".", "entityindex": -1, "wordindex": 8}, {"entitiy": "OPERATOR", "word": "Türkcell", "entityindex": 2, "wordindex": 9}, {"entitiy": "OTHER", "word": "ise", "entityindex": -1, "wordindex": 10}, {"entitiy": "OTHER", "word": "yetersiz", "entityindex": -1, "wordindex": 11}, {"entitiy": "OTHER", "word": "seviyede", "entityindex": -1, "wordindex": 12}, {"entitiy": "OTHER", "word": "değil", "entityindex": -1, "wordindex": 13}, {"entitiy": "OTHER", "word": ".", "entityindex": -1, "wordindex": 14}]
    # print(f'................{nerResponse}')
    df_ner_response = pd.DataFrame.from_dict(nerResponse)

    # Get Dependency
    text = ' '.join(df_ner_response.word.tolist())

    text_sentences, indices = getSentencesWithIndices(text)
    print(text_sentences)

    out_sentences = []
    for i in range(len(text_sentences)):
        start_idx, end_idx = indices[i]
        sub_text = text_sentences[i]

        df_ner_sub = df_ner_response[df_ner_response.wordindex.between(start_idx, end_idx)]
        print(df_ner_sub.head())

        print(f'..................... {type(spacyNlp)}')

        # Run spacy nlp Dependecy Parser
        spacyNlp.tokenizer = WhitespaceTokenizer(spacyNlp.vocab)
        doc = spacyNlp(sub_text)

        exclude_tokens = getExcludeTokens(doc)

        df_dependency = outDependencyForm(doc, start_idx)

        # Merge Ner results and dependency parser results
        df_sentences = pd.merge(df_ner_sub, df_dependency, on='wordindex', how='left')
        print(df_sentences.head(20))

        ##### exclude LOC,GPE,PERSON
        print(f'======================')
        df_sentences['entitiy'] = (df_sentences[['entitiy', 'word']].
                                  apply(lambda row: 'OTHER' if (row['word'] in exclude_tokens) else row['entitiy'], axis=1))
        print(df_sentences.head(20))
        print(f'======================')
        ######


        ###### exclude HIZMET entity
        #df_sentences['entitiy'] = df_sentences[df_sentences['entitiy'] = df_sentences['entitiy'].apply(lambda x: 'OTHER' if x == 'HIZMET' else x) 'entitiy'].apply(lambda x: 'OTHER' if x == 'HIZMET' else x)
        all_indexes = df_sentences[df_sentences['entitiy'] == 'HIZMET']['entityindex'].unique().tolist()
        print(f'=======================')
        print(all_indexes)
        exclude_indexes = []
        for idx in all_indexes:
            for sub_index, sub_row in df_sentences[df_sentences['entityindex'] == idx].iterrows():
                print(sub_row['entitiy'])
                if sub_row['entitiy'] != 'HIZMET':
                    exclude_indexes.append(sub_row['entityindex'])
        exclude_indexes = list(np.reshape(list(exclude_indexes), -1))

        df_sentences['entitiy'] = (df_sentences[['entitiy', 'entityindex']].
                                  apply(lambda row: 'OTHER' if (row['entityindex'] in exclude_indexes and row['entitiy'] == 'HIZMET')
                                                            else row['entitiy'], axis=1))


        print(exclude_indexes)
        print(f'=======================')
        ######

        ######
        #df_sentences['entitiy'] = (df_sentences[['entitiy', 'word']].
        #                            apply(lambda row: 'OTHER' if (row['entitiy'] != 'OTHER' and len(row['word']) <= 2 and row['word'] not in ('tt', 'tr', 'tv'))
        #                                                      else row['entitiy'], axis=1))
        ######


        # Split sentences by dependencies
        sentences = splitSentencesByDependecies(df_sentences)
        print(f'-----------------------')
        print(f'sentences are : {sentences}')
        print(f'-----------------------')
        out_sentences.append(sentences)

    print(f'==================== {out_sentences}')
    # print(sentences)
    # get Sentiments results by sentences and entities
    result = makeResult(out_sentences=out_sentences)
    # result = { "entity_list": [ "Türk Telekom", "Türkcell"], "results": [{ "entity": "Türk Telekom", "sentiment": "olumlu" },{ "entity": "Türkcell", "sentiment": "olumlu" } ]}

    #Append each response
    with open('outputs/requests.txt', 'a+') as f:
        f.write(json.dumps(result,  indent=0) + '\n')

    return json.loads(result)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5500)
