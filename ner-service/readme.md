Varlık İsmi Çıkarma

2024 Teknofest Doğal Dil İşleme (NLP) senaryo kategorisinde, Türkcell gibi mobil operatörler ve bunlarla ilişkili olan ürünler, paketler ve uygulamaları  (Superonline, Platinum Paket, BİP, Fizy, Lifebox, Müşteri Hizmetleri vb.) kapsayan, metinler içinden ilgili varlıkları çıkarmak amacıyla geliştirlmiş olan projedir.

Geliştirilen model için veriler X platformundan üzerinden @Turkcell varlığına ilişkin yapılan yorumlar toplanarak ve sikayetvar web sayfası üzerinden yapılan scrabing ile veri alınması süreçleri ile temin edilmiştir. Elde edilen 20700 adet veri, açık kaynak Doccano uygulaması ile etiketlenmiş; bu etiketleme işleminde daha detaylı analiz yapılmasını sağlayabilmek adına etiketler, "OPERATOR, URUN, HIZMET, UYGULAMA ve PAKET" gibi başlıklara ayrılmıştır.

Örnek bir etiketleme yapısı şu şekildedir: 
{
  "id": 922, 
  "text": "Şu hayatta 3 şeyden nefret ederim 1.Götoşlar 2.Turkcell 3.TTNET .Bimcell'e geççem mk :D mldfjsşgş", 
  "label": [[47, 55, "OPERATOR"], [58, 63, "OPERATOR"], [65, 72, "OPERATOR"]], 
  "Comments": []
}

Etiketlenen verilerin modeller SpaCy ve Bert gibi modellerde kullanımını kolaylaştırmak amacıyla "ner-service/utils/Json2Conll.ipynb" adresinde notebook dosyasında ki yapı geliştirilmiş ve veriler jsonL formatından conLL formatına dönüştürülmüştür.

Bu süreçte özellikle şikayetvar verilerini işlerken karşımıza uzun metinler içeren veriler çıkmıştır. Bu durum ileride model geliştirme aşamasında "input_token_size" parametresi açısından problem teşkil edebilirdi. Ayrıca daha önceki tecrübelerimizden edindiğimiz bilgiler NER problemleri için uzun cümleler yerine anlamlı daha kısa cümleler kurulmasının daha başarılı sonuçlar ürettiğini göstermiştir. Bu sebeble sikayetvar verilerini cümlelere ayırmak için (veriler incelendiğinde imla kurallarına uygun cümleler olduğu gözlemlendi) "ner-service/utils/chuningLongText.ipynb" adresinde bulunan notebook dosyası içerisinde chunking yapısı geliştirildi.

Tüm bu süreçler sonucunda elde edilen veri dosyası "ner-service/data/dataset.conll" adresinde bulunmaktadır. Son durumda tag ve örnek sayıları aşağıdaki gibi oluşmuştur.

![Screenshot from 2024-08-06 15-25-31](https://github.com/user-attachments/assets/65f6d1c0-74a3-46d2-ac25-a0693ab6afcd)





Veri, gerek LSTM, gerek SpaCy ve gerekse de BERT mimarileri 
