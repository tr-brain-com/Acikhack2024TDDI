# Libraries
import streamlit as st
from PIL import Image

# Confit
st.set_page_config(page_title='AçıkHack2024TDDI', page_icon=':bar_chart:', layout='wide')

# Title
st.title('Teknofest 2024 Türkçe Doğal Dil İşleme Senaryo Kategori Yarışması')

# Content

st.write(
    """
    Türkiye Açık Kaynak Platformu, Türkçe Doğal Dil İşleme konusunda farkındalık yaratmak amacıyla yarışma düzenleniyor.
    Entity Bazlı Duygu Analizi Yarışması, katılımcıların geniş bir yelpazedeki firmalardan
    veya kurumlardan gelen müşteri geri bildirimlerini analiz etmelerini ve bu yorumlardaki
    duyguları belirli hizmet yönleri veya ürün özellikleri ile ilgili olarak sınıflandırmalarını
    hedeflemektedir. 
    
    Bu kullanıcı arayüzü, bu kapsamda geliştirilmiş olup çalışmalarımız sonucunda elde edilen model için tahmin, 
    canlı izleme ve geri bildirim gibi işlemleri gerçek ortamda test etmek amacıyla **Brain-Tr** takımı 
    tarafından geliştirilmiştir.

    """
)

st.subheader('Metodoloji')
st.write(
    """
    
    Görev, katılımcılardan verilen yorumları öncelikle entity'e göre
    sıralamalarını, sonrasında ise entity'lerin sunduğu hizmetler veya ürünlerle ilgili
    yorumlardaki duyguları (olumlu, olumsuz veya nötr) belirlemelerini istemektedir. Bu
    yarışma, herhangi bir sektörden birden fazla entity hakkında yorumları içerebilir ve
    katılımcıların yorumları doğru entity'ye atfetme ve ilgili hizmet yönlerine göre duygu
    analizi yapma becerilerini test eder
    
    """
)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Data Analyst: [@Brain-Tr](https://github.com/tr-brain-com)**', icon="💡")
with c2:
    st.info('**GitHub: [@Brain-Tr](https://github.com/tr-brain-com)**', icon="💻")
with c3:
    st.info('**Data :  [Eğitim Veri Kümesi](https://github.com/tr-brain-com/acikhack2023TDDI/tree/main/data)**', icon="🧠")