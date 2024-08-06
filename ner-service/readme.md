<B>Varlık İsmi Çıkarma</b>

2024 Teknofest Doğal Dil İşleme (NLP) senaryo kategorisinde, Türkcell gibi mobil operatörler ve bunlarla ilişkili olan ürünler, paketler ve uygulamaları  (Superonline, Platinum Paket, BİP, Fizy, Lifebox, Müşteri Hizmetleri vb.) kapsayan, metinler içinden ilgili varlıkları çıkarmak amacıyla geliştirlmiş olan projedir.

Geliştirilen model için veriler X platformundan üzerinden @Turkcell varlığına ilişkin yapılan yorumlar toplanarak ve sikayetvar web sayfası üzerinden yapılan scrabing ile veri alınması süreçleri ile temin edilmiştir. Elde edilen 20700 adet veri, açık kaynak Doccano uygulaması ile etiketlenmiş; bu etiketleme işleminde daha detaylı analiz yapılmasını sağlayabilmek adına etiketler, <b><u>"OPERATOR, URUN, HIZMET, UYGULAMA ve PAKET"</u></b> gibi başlıklara ayrılmıştır.

Örnek bir etiketleme yapısı şu şekildedir: <br>
{<br>
  "id": 922, <br>
  "text": "Şu hayatta 3 şeyden nefret ederim 1.Götoşlar 2.Turkcell 3.TTNET .Bimcell'e geççem mk :D mldfjsşgş", <br>
  "label": [[47, 55, "OPERATOR"], [58, 63, "OPERATOR"], [65, 72, "OPERATOR"]], <br>
  "Comments": []<br>
}<br>

Etiketlenen verilerin modeller <b>SpaCy ve Bert</b> gibi modellerde kullanımını kolaylaştırmak amacıyla "ner-service/utils/Json2Conll.ipynb" adresinde notebook dosyasında ki yapı geliştirilmiş ve veriler <b>jsonL</b> formatından <b>conLL</b> formatına dönüştürülmüştür.

Bu süreçte özellikle şikayetvar verilerini işlerken karşımıza uzun metinler içeren veriler çıkmıştır. Bu durum ileride model geliştirme aşamasında <b>"input_token_size"</b> parametresi açısından problem teşkil edebilirdi. Ayrıca daha önceki tecrübelerimizden edindiğimiz bilgiler NER problemleri için uzun cümleler yerine anlamlı daha kısa cümleler kurulmasının daha başarılı sonuçlar ürettiğini göstermiştir. Bu sebeble sikayetvar verilerini cümlelere ayırmak için (veriler incelendiğinde imla kurallarına uygun cümleler olduğu gözlemlendi) "ner-service/utils/chuningLongText.ipynb" adresinde bulunan notebook dosyası içerisinde chunking yapısı geliştirildi.

Tüm bu süreçler sonucunda elde edilen veri dosyası "ner-service/data/dataset.conll" adresinde bulunmaktadır. Son durumda tag ve örnek sayıları aşağıdaki gibi oluşmuştur.

![Screenshot from 2024-08-06 15-25-31](https://github.com/user-attachments/assets/65f6d1c0-74a3-46d2-ac25-a0693ab6afcd)

Veriler kullanıma hazır hale getirildikten sonra bu alanda (NER) yapılan çalışmalar incelenmiş ve LSTM, SPACY ve BERT gibi mimarilerle başarılı sonuçlar alınabileceği gözlemlenmiştir. Yaptığımız local testlerde LSTM ve SPACY mimarileri BERT mimarisine göre oldukça kötü sonuçlar üretmiştir. BERT ile transfer öğrenme tekniği kullanılarak "savasy/bert-base-turkish-ner-cased" yapısı üzerine inşaa ettiğimiz ve eğitimi tamamladığımız yapı, denemelerde en iyi skorları üretmiş; eğitim ortamında olmayan gerçek ortam verileri ile yaptığımız testlerde de başarısını göstermiştir.


Eğitim için veri, %90' a %10 olarak ayrılmıştır.<br>

train_df, val_df = train_test_split(data, test_size=0.10)<br>


## Bu işlemle 165738 kayıt eğitim için 18416 adet kayıt ise doğrulama için kullanılmıştır.##

## BERT modeli için kullanılan parametreler: ##

input_token_size = 256  <br>
batch_size = 32<br>
epoch = 6<br>
max_grad_num = 1.0<br>
optimizer = AdamW<br>
learning_rate = 3e-5<br>
epsilon = 1e-8<br>

## Eğitime İlişkin Açıklamalar: ##

![Screenshot from 2024-08-06 15-39-10](https://github.com/user-attachments/assets/38a6d53f-c334-4c9e-9ff0-d3e95a408029)

Yukarıda belirtilen öğrenme eğrisinden ve aşağıda belirtilen eğitim sonuçlarından da anlaşılacağı üzere modelin öğrenmesi 3-4 dönemden sonra durmakta ve model "OTHER" ifadelerinin orantısız şekilde fazla olmasından dolayı overfit olmaktadır. 

## Model eğitim sonuçları şu şekildedir: ##

![Screenshot from 2024-08-06 15-49-16](https://github.com/user-attachments/assets/a62c8e8e-2b72-4ada-b6b7-aac0a73885e1)


## Gerçek Verilerle Yapılan Denemeler: ##

<b>Text: </b>

"Avea neden hep Turkcell in reklamlarına diss atıyo"

<b>Sonuç:</b>

![Screenshot from 2024-08-06 16-30-51](https://github.com/user-attachments/assets/ec52f601-2066-4e2c-a9e6-565d05e12799)

<b>Text:</b>

"gnçtrkcll üyeleri için kampanya sürüyor. üyeyseniz bu fırsatı kaçırmayın.#sanakapakolsun gnctrkcll"

<b>Sonuç:</b>

![Screenshot from 2024-08-06 16-32-31](https://github.com/user-attachments/assets/9d41355d-5345-429f-9bc4-94a0e2faef00)


<b>Text:</b>

"Bir @YouTube oynatma listesine video ekledim: Müşteri hizmetleri için sizde buna Turkcell BiP Ön Bakış üzerinde bakabilirsiniz."

<b>Sonuç:</b>

![Screenshot from 2024-08-06 16-35-06](https://github.com/user-attachments/assets/2a9780c4-5c8c-4e78-bbae-587709e86f7b)


Yukarıda ki metriklerden ve açıklamalardan da görüldüğü üzere bulduğumuz veriler, etiketleme politikamız ve model seçimimiz, detaylı varlık çıkarımı için oldukça etkileyici sonuçlar vermiştir.

"OTHER" ifadeler Accuracy anlamında modeli overfit duruma  götürsede F1 score bize gerçek değeri vermekte; ayrıca eğitim vericinin haricind edindiğimiz gerçek dünya verileri ile de model başarısını göstermektedir.


<b>Model indirmek için lütfen iletişime geçin.</b>

https://drive.google.com/drive/folders/1H0nGnQlnkLIxpahd4rLhQ1uWwYWjZ9v7








