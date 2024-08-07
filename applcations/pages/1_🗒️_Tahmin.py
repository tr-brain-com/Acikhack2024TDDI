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
        if response.status_code == 200:
            return response.json()
        else:
            st.info(f"İşleminiz gerçekleştirilemedi...")

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

            predict_url = "http://127.0.0.1:8000/predict"
            predict_value = predict(text_input, predict_url)

            entity = predict_value.get('entity_list')
            results = predict_value.get('results')
            #p_score = predict_value.get('p_score')


            temp_entity_data = []
            if entity:
                if len(entity) > 0:
                    for res in results:
                        temp_entity_data.append([res['entity'], res['sentiment']])
                        #st.info(f"{res['entity']},  {res['sentiment']}")
                else:
                    st.info("Bu giriş için bir varlık tahmininde bulunamadım.")
            st.info(f"{temp_entity_data}")


            severity_predict_url = "http://127.0.0.1:8001/predict"
            severity_predict_value = predict(text_input, severity_predict_url)


            severity = severity_predict_value.get('severity')
            action = severity_predict_value.get('action')

            if severity:
                st.success(f"{severity},  {action}")


            reason_predict_url = "http://127.0.0.1:8002/predict"
            reason_predict_value = predict(text_input, reason_predict_url)


            reason = severity_predict_value.get('severity')

            if severity:
                st.error(f"Sebep ,  {reason}")


text_input_screen()
