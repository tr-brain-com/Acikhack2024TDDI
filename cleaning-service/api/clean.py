import json
import logging
import os
import re

class CLEANING:
    def __init__(self, raw_text, contractions, stopwords):
        self.Text = raw_text.replace("İ", "i")
        self.Contractions = contractions
        self.Stopwords = stopwords

        if os.path.exists("stopword.txt"):
            with open("stopword.txt", "r") as file:
                self.Stopwords_List = file.read().split("\n")
        else:
            logging.error("Stopword dosyası bulunamadı.")
            self.Stopwords_List = []

        if os.path.exists("contractions.json"):
            with open("contractions.json") as json_file:
                self.Contractions_List = json.load(json_file)
        else:
            logging.error("Contractions dosyası bulunamadı.")
            self.Contractions_List = {}

    def lowercase(self, text):
        return text.lower()

    def split(self, text):
        return text.split()

    def tweet_tag_clean(self, text):
        temp_text = re.sub("@[A-Za-z0-9_]+", "", text)
        return ' '.join(word for word in temp_text.split() if not word.startswith("#"))

    def http_clean(self, text):
        regex = re.compile(r'<[^>]+>')
        temp_text = regex.sub('', text)
        return re.sub(r'http\S+', '', temp_text)

    def numeric_clean(self, text):
        return re.sub("[0-9]", "", text)

    def special_char_clean(self, text):
        return re.sub(r'[_"\-;%()|+&=*%.”“’,!?:#$@\[\]/]', '', text)

    def stopwords_clean(self, text):
        return ' '.join(word for word in text.split() if word not in self.Stopwords_List)

    def single_characters_clean(self, text):
        return ' '.join([w for w in text.split() if len(w) > 1])

    def clean(self):
        temp_text = self.Text
        temp_text = self.lowercase(temp_text)
        temp_text = self.split(temp_text)

        if self.Contractions:  # Kısaltmaları dönüştür
            new_text = []
            for word in temp_text:
                if word in self.Contractions_List:
                    new_text.append(self.Contractions_List[word])
                else:
                    new_text.append(word)
            temp_text = " ".join(new_text)

        temp_text = self.tweet_tag_clean(temp_text)  # tweet ve tag temizle
        temp_text = self.http_clean(temp_text)  # http tag temizle
        temp_text = self.numeric_clean(temp_text)  # numeric değerleri temizle
        temp_text = self.special_char_clean(temp_text)  # special karakterleri temizle

        if self.Stopwords:
            temp_text = self.stopwords_clean(temp_text)  # stopword kelimeleri temizle

        temp_text = self.single_characters_clean(temp_text)  # special karakterleri ve emojileri temizle

        temp_text = temp_text.lstrip().rstrip()  # text baş ve sonundaki boşlukları at

        return temp_text


if __name__ == "__main__":
    texts = ["20 dk 1 GB internet 500 mb sadece kaşar turkcell de düşer. Oç çocukları.",
             "turkcell lanet olsun cok kaziksin amk",
             "80 tl cepfaturasi mi olur hani hayat paylasinca guzeldi. Allah belani versin turkcell",
             "@coskununyeri en cOmertte turkcell.",
             "@turkcell #t70benimolsun CUnkU 4.5g teknolojisi ve turkcell kalitesi ve gUvencesiyle..."]

    for text in texts:
        print(CLEANING(text, True, True).clean())
