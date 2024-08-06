import logging
import os
import json
import torch
from transformers import  AutoModelForTokenClassification,  AutoTokenizer
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn

app = FastAPI(title="BRAIN-TR Varlık İsmi Çıkarım")

tokenizer = None
model = None
model_name = None

class Item(BaseModel):
    text: str = Field(..., example="""Al iste Ttnet bitti Turkcell başladı. Bu ne lan mesajlar niye iletilmiyooooooooor.""")

def token_analizer(tokens, label_indices):

    tags = ['APP', 'OPERATOR', 'PRODUCT', 'HIZMET', 'O', 'PACKAGE', 'PAD']
    new_tokens, new_labels = [], []
    for token, label_idx in zip(tokens, label_indices[0]):
        if token.startswith("##"):
            new_tokens[-1] = new_tokens[-1] + token[2:]
        else:
            new_labels.append(tags[label_idx] if label_idx<= len(tags) else "OTHER")
            new_tokens.append(token)
    return new_tokens, new_labels

def output_analizer(new_tokens, new_labels):
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
    return outputs
@app.on_event("startup")
def startup_event():
    try:
        global tokenizer
        global model
        global model_name
        model_name = "api/models"

        tokenizer = AutoTokenizer.from_pretrained(model_name, do_lower_case=False)
        model = AutoModelForTokenClassification.from_pretrained(model_name)

    except Exception as e:
        logging.error(f"Model not loaded! Error : {e}")
    logging.info("Server Running Worker PidID : {0}".format(os.getpid()))


@app.on_event("shutdown")
def shutdown_event():
    logging.info("Server Shutdown PidID : {0}".format(os.getpid()))

@app.post("/predict/")
async def predict(item: Item):
    global tokenizer
    global model

    sentence = item.text
    tokenized_sentence = tokenizer.encode(sentence)
    input_ids = torch.tensor([tokenized_sentence])

    with torch.no_grad():
        output = model(input_ids)


    label_indices = np.argmax(output[0].to("cpu").numpy(), axis=2)

    tokens = tokenizer.convert_ids_to_tokens(input_ids.to('cpu').numpy()[0])
    new_tokens, new_labels = token_analizer(tokens, label_indices)

    return output_analizer(new_tokens, new_labels)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

