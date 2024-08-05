import json
import requests
import streamlit as st

st.set_page_config(page_title='Teknofest 2024 Türkçe Doğal Dil İşleme Senaryo Kategori Yarışması ', page_icon=':bar_chart:', layout='wide')
st.title('🗒️ Entity Bazlı Duygu Analizi')

with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.subheader('Söylem Tespiti')

def text_input_screen():
    def predict(text, predict_url):
        predict_appname = "acikhack2024TDDI Predict Apps"
        newheaders = {'Content-type': 'application/json', 'AdaletApplicationName': predict_appname}

        predict_post_data = {
            "text": text
        }

        response = requests.post(predict_url, headers=newheaders, data=json.dumps(predict_post_data), verify=False)
        return response.json()

    def callback():
        pass

    text_input = st.text_area(label="Sınıflandırılacak metin girişi", on_change=callback, key="predict_input_text", max_chars=200, height=200)
    submit = st.button(label="Metni Değerlendir")

    if submit:
        if len(text_input) == 0:
            st.write('Değerlendirme için bir metin giriniz.')
        else:
            predict_url = "http://127.0.0.1:8000/predict"
            predict_value = predict(text_input, predict_url)

            sentiment = predict_value.get('sentiment')
            p_score = predict_value.get('p_score')

            class_desc = {"nötr": " İçerik nötr ifade bulunmaktadır.",
                          "olumlu": "İçerik olumlu ifade bulunmaktadır.",
                          "olumsuz": "İçerik olumsuz ifade bulunmaktadır."}

            if sentiment:
                summary = f"{sentiment} (Skor: {p_score})"
                st.info(f"BERT : {class_desc.get(sentiment, 'Belirlenemedi')}  ( {summary} )")
            else:
                st.info("Bu metin için bir tahminde bulunamadım.")

text_input_screen()
