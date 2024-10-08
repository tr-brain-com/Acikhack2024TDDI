#  🇹🇷 Acikhack2024TDDI
Teknofest 2024 Türkçe Doğal Dil işleme Senaryo Kategorisi

# 🇹🇷 Application

![Braintr-720](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/brain_tr_app.gif)

Streamlit ile hazırlanmış olan uygulamamız için ayrıntılı bilgi için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/applcations/readme.md).

#  🇹🇷 Data Minning
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/beautifulsoup.jpg" height="300">
</p>

Veri madenciliği, büyük veri setlerinden anlamlı ifadeler, ilişkiler ve bilgiler çıkarmak için kullanılan bir süreçtir. Veri madenciliği, veri hazırlama, model oluşturma, değerlendirme ve sonuçları yorumlama gibi adımları içerir.
BeautifulSoup ve Scrapy: Web kazıma (web scraping) için kullanılır. İnternetten veri çekmek ve analiz etmek için kullanışlıdır. BeautifulSoup, Python'da HTML ve XML dosyalarını ayrıştırmak ve analiz etmek için kullanılan bir kütüphanedir. Web sayfalarından veri çekmek, web kazıma işlemlerinde sıklıkla tercih edilir. HTML ve XML dosyalarını kolayca ayrıştırır. Belgelerdeki elementlere, etiketlere ve niteliklere hızlı ve kolay erişim sağlar.
Belgeleri ağaç yapısı (parse tree) olarak temsil eder ve bu sayede belirli elementleri seçip işlemek kolaylaşır.
2024 Teknofest Türkçe Doğal Dil İşleme kategorisi için veri madenciliği (data mining) kod bloğunu adım adım incelemek için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/dataMinning/readme.md).

#  🇹🇷 Data Stats
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-07-30%2008-46-02.png" height="300">
</p>

Teknofest yarışması kapsamında, X (Twitter) platformu, ŞikayetVar web sayfası ve Yıldız Teknik Üniversitesi'nin duygu analizi çalışmasından elde edilen veri setleri birleştirilerek toplamda 20,700 veri noktası içeren kapsamlı bir veri seti oluşturulmuştur. Bu veri seti, çeşitli ürünler ve hizmetlerle ilgili kullanıcı geri bildirimlerini ve şikayetleri kapsamaktadır.

Veri Dağılımı:

    Olumsuz İfadeler: %60
    Nötr İfadeler: %20
    Olumlu İfadeler: %20


Veri seti, genel eğilimleri ve kullanıcıların duygusal tepkilerini anlamak için önemli bir başlangıç noktasıdır. Bu veriler, gelecekteki hizmet iyileştirmeleri, müşteri deneyimini geliştirme stratejileri ve pazarlama kampanyaları için değerli içgörüler sağlayabilir. 

Veri seti analizi için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/stats/readme.md).



# 🇹🇷 Data Cleanning
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/cleaning.png" height="300">
</p>
Temizleme servisi (Cleaning service), bu çalışmaya uygun olarak yapılan denemeler sonucunda bir standart belirlenerek çoğu bölümü isteğe bağlı olarak kullanılabilecek şekilde geliştirilmiştir. 

Temizleme servisi hakkında daha ayrıntılı bilgi almak ve detaylar için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/cleaning-service/readme.md).


# 🇹🇷 Named Entity Recognition

2024 Teknofest Doğal Dil İşleme (NLP) senaryo kategorisinde, Turkcell gibi mobil operatörler ve bunlarla ilişkili olan ürünler, paketler ve uygulamaları (Superonline, Platinum Paket, BİP, Fizy, Lifebox, Müşteri Hizmetleri vb.) kapsayan, metinler içinden ilgili varlıkları çıkarmak amacıyla geliştirilmiş olan projedir.

Geliştirilen model için veriler X platformu üzerinden @Turkcell varlığına ilişkin yapılan yorumlar toplanarak ve sikayetvar web sayfası üzerinden yapılan kazıma ile veri alınması süreçleri ile temin edilmiştir. Elde edilen 20700 adet veri, açık kaynak Doccano uygulaması ile etiketlenmiş; bu etiketleme işleminde daha detaylı analiz yapılmasını sağlayabilmek adına etiketler, <b><u>"OPERATOR, URUN, HIZMET, UYGULAMA ve PAKET"</u></b> gibi başlıklara ayrılmıştır.


Tüm bu süreçler sonucunda elde edilen veri dosyası "ner-service/data/dataset.conll" adresinde bulunmaktadır. Son durumda etiket ve örnek sayıları aşağıdaki gibi oluşmuştur.

![Screenshot from 2024-08-06 15-25-31](https://github.com/user-attachments/assets/65f6d1c0-74a3-46d2-ac25-a0693ab6afcd)

Eğitim için veri, %90' a %10 olarak ayrılmıştır.<br>

train_df, val_df = train_test_split(data, test_size=0.10)<br>


## Eğitim Sonuçları ##

![Screenshot from 2024-08-06 15-49-16](https://github.com/user-attachments/assets/a62c8e8e-2b72-4ada-b6b7-aac0a73885e1)

## Gerçek Verilerle Deneme ##

<b>Text:</b>

"Bir @YouTube oynatma listesine video ekledim: Müşteri hizmetleri için sizde buna Turkcell BiP Ön Bakış üzerinde bakabilirsiniz."

<b>Sonuç:</b>

![Screenshot from 2024-08-06 16-35-06](https://github.com/user-attachments/assets/2a9780c4-5c8c-4e78-bbae-587709e86f7b)


Varlık İsmi Çıkarımı (NER) aşamasını adım adım incelemek için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/tree/main/ner-service).

# 🇹🇷 Bağımlılık Analizi (Dependency Parsing)

Bu bölüm, problem tanımı uyarınca cümle içerisinde geçen farklı varlıklara yönelik duyguları tespit etmek amacıyla geliştirilmiştir. Yapılan araştırmalar ve gerçekleştirilen çalışmalar incelendiğinde problem çözümüne yönelik olarak <b>Yönelim Tabanlı (Aspect Based)</b> ve <b>Varlık Tabanlı (Entity Based)</b> olarak iki farklı yöntem geliştirildiği; bu yöntemlerin seçimi konusunda da alana özgü verilerin yapısının etkili olduğu fark edilmiştir.<br>

<b>Yönelim Tabanlı (Aspect Based)</b>, bir cümlede veya belgede belirtilen belirli yönlerle ilişkili duyguyu belirleme görevini ifade eder. <br>

<b>Varlık Tabanlı (Entity Based)</b> olarak ifade edilen yapı ise cümle içinde belirlenen varlıklara yönelen duyguların tespitini sağlamayı ifade eder.<br>

Bu çalışma için ürettiğimiz, geliştirdiğimiz veri (ayrıntılı bilgi stats içerisinde mevcuttur), hem entity hemde aspect tabanlı hibrit bir yapının ortaya konulmasını bizim için gerekli kılmıştır. Bu noktada <b>Bağımlılık Analizi (Dependency Parsing)</b> olarak bilinen bir dile ait cümle yapılarının detaylı şekilde incelenmesi ve yorumlanması gerekmiştir. Bağımlılık Analizi ile cümle bölümlendirmesi ve varlık tabanlı ayrıştırma birlikte öğrenilir. Mevcut problemde varlık bazlı veya varlığa yönelik duyguları tespit etmek amacıyla SpaCy kullanarak kural tabanlı bir yapı inşa edilmiştir. Bu kural tabanlı yapı, metinlerin standart cümle yapısına uymayacağı (X verileri vb.) fikrinden hareketle ortaya çıkarılmış, metin içerisinde ki varlıklara yönelen duyguların tespitinde oldukça başarılı sonuçlar elde edilmiştir.<br>

Çalışma sonrası gerçek bir örneğe ilişkin sonuçlar şu şekildedir:<br>

<b>text :</b><br> 
tt çekmiyor vodafone hizmeti rezalet ötesi kesinti oluyor. Turkcell fiyat farkını hak ediyor.<br>

<b>sonuç :</b> 

![image](https://github.com/user-attachments/assets/a1c861d4-8ed4-4260-b21e-0f1a274eba9c)

Ayrıntılı bilgi için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/Dependency%20Parsing/readme.md).


# 🇹🇷 Sentiment Analysis

Veri seti elde ettiğimiz kaynaklar için Stats kısmında ayrıca anlatılmaktadır. Ayrıntılı bilgi için Stats kısmını tıklayınız.<br>

BERT tabanlı bir model kullanarak Türkçe metinlerde duygu analizi yapmaktadır. Proje kapsamında k-fold çapraz doğrulama yöntemi uygulanmıştır. "bert-base-turkish-cased" modeli, Türkçe dilinde büyük ve küçük harf ayrımını dikkate alır. Bu, dil bilgisi ve kelime anlamları açısından önemli olabilir. Cased model kullanmak, özellikle özel isimlerin doğru şekilde anlaşılması ve sınıflandırılması açısından avantaj sağlar.

Her modelimiz ayrı ayrı rest servis olcak şekliyle hazırlanmıştır. Model başarı değerleri aşağıdaki gibidir. 
| Sınıf        | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| 0  (Nötr)          | 0.846     | 0.824  | 0.861    | 577     |
| 1  (Olumlu)          | 0.86     | 0.872  | 0.885    | 352     |
| 2  (0lumsuz)          | 0.920     | 0.910  | 0.915    | 1305    |
| **Accuracy** | |        |        **0.901**   | **2234**|
| **Macro Avg**| **0.814** | **0.821** | **0.818** | **2234** |
| **Weighted Avg** | **0.855** | **0.854** | **0.854** | **2234** |

Model eğitimi ve Rest Api kodlarının ayrıntılı açıklaması için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/Sentiment%20Analysis/readme.md).

# 🇹🇷 Aciliyet (Severity) Sınıflandırması
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-08-02%2021-03-13.png" height="600">
</p>

2024 Teknofest Doğal Dil İşleme (NLP) senaryo kategorisinde, Turkcell ve ürünleri (Superonline, Platinum Paket, BİP, Fizy, Lifebox vb.) hakkında kullanıcı yorumlarına dayalı özgün bir entity bazlı duygu analizi gerçekleştirilmiştir. Bu çalışmada, yalnızca yorumların duygusal tonu belirlenmemiş, aynı zamanda yorumların taşıdığı önem veya aciliyet düzeyini belirtmek için "severity" adı verilen ekstra bir kategori de eklenmiştir. "Severity" kolonu, metinde tartışılan konunun aciliyet veya önem derecesini ifade eder; 0 'aciliyeti bulunmayan', 1 'orta derecede acil' ve 2 'acil' bir durumu belirtir. Ayrıntılı bilgi ve kod için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/severity%20Classification/readme.md).

# 🇹🇷 Reason Classification
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-08-02%2021-21-59.png" height="600">
</p>

Teknofest 2024'teki Doğal Dil İşleme (NLP) senaryo kategorisi yarışmasında katıldığımız proje, varlık bazlı duygu analizi üzerine odaklanmaktadır. Projemizde, Turkcell ve ürünleri hakkında yazılan metinlerde olumsuzluğa sebep olan kategorilerin tespitini amaçlayarak özgünlük sağlamak için veri setine "sebep (reason)" kolonu eklenmiştir. Bu kolon, kullanıcıların olumsuz duygu bildirdiği durumlarda hangi kategoriye (örneğin bayi, fatura, kampanya) dair olumsuzluk yaşadıklarını belirlememize olanak tanımaktadır. Ayrıntılı bilgi ve kod için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/reason%20classificaiton/readme.md).


#  🇹🇷 Contribution
2024 Teknofest Türkçe Doğal Dil İşleme senaryo kategorisi yarışmasında, projemiz varlık tabanlı duygu analizine odaklanmaktadır. Bu kapsamda, X ve Şikayet Var sayfalarından veri madenciliği yaparak kendi verilerimizi oluşturduk. Yarışmanın ana hedefi, metin içerisindeki varlıkları tespit etmek ve bu varlıklara ait duygu analizini yaparak sonuçları olumlu, olumsuz ve nötr olarak sınıflandırmaktır. Analizimizin kapsamını ve derinliğini artırmak için veri setimize ek kolonlar ekledik ve her biri aşağıda açıklanmaktadır


| Category       | Description                                                              
| ----------     | ---------------------------------------------
| Entity Listesi          | Metinde geçen varlıkların listesini içerir. Yaklaşık 100 farklı varlık tespit edilmiş, böylece analizin geniş bir kapsama sahip olmasını sağlanmıştır.
| Target      | Tespit edilen varlıkla ilişkili duygu burada olumlu, olumsuz veya nötr olarak sınıflandırılır. Bu, yarışmanın gereksinimlerine uygun olarak belirlenmiştir.       
| Severity         | Metinde tartışılan konunun aciliyet veya önem derecesini belirtir. 0 'aciliyeti bulunmayan', 1 'orta derecede acil' ve 2 'acil' aksiyonu ifade eder.           
| Reason         | Olumsuz duygular için belirlenmiştir, sorunun kaynağını belirler. Örneğin, fatura, ağ (network) sorunları, mobil numara taşıma (mnp) gibi. Bu, müşteri memnuniyetsizliğinin temel nedenini anlamamıza yardımcı olur    
| Muhatap         | Girdinin ana muhatabının Turkcell olup olmadığını belirtir.     
| Mobil         | Sorunun mobil hat ile ilgili olup olmadığını belirtir      
| Sabit         | Sorunun sabit hat ile ilgili olup olmadığını belirtir.      
| Ek Paket         |  Sorunun ek paketlerden kaynaklanıp kaynaklanmadığını belirtir.   
| Kampanya        |   Sorunun bir kampanyadan (örneğin, promosyon teklifleri, ekstra GB) kaynaklanıp kaynaklanmadığını belirtir.
| Diğer Ürün/Uygulama         |  Turkcell'in hangi uygulama veya ürününden (örneğin, BIP, Fizy, Platinum) kaynaklandığını belirler.   
| Reklam         |  Turkcell'in reklamları, sponsorlukları veya boykotları ile ilgili şikayetleri kaydeder.      
| Çağrı Merkezi         |Çağrı merkezi ve teknik destek ile ilgili şikayetleri bu kolonda belirtilir.     
| Bayi         |      Satış noktaları ve mağazalarla ilgili şikayetleri kaydeder.

Bu ek kolonlar sayesinde, daha ayrıntılı ve eyleme geçirilebilir bir duygu analizi sunmayı amaçlıyoruz. Yaklaşımımız, yarışmanın gereksinimlerini karşılamakla kalmayıp, aynı zamanda Turkcell'in müşteri şikayetlerine daha etkili bir şekilde yanıt vermesine ve genel müşteri memnuniyetini ve hizmet kalitesini artırmasına yardımcı olabilecek değerli içgörüler sunmaktadır. Bu geliştirilmiş veri seti yapısı, müşteri geri bildirimlerinin daha derinlemesine anlaşılmasını sağlar ve hedefe yönelik müdahaleler ile stratejik karar alma süreçlerini destekler.

# 🇹🇷 Results
Bu çalışmada, girdi içerisinde farklı varlıklara ilişkin duyguların tespit edilmesi konusunda oldukça geniş bir literatür taraması yapılmış, farklı yöntemler denenmiş ve dilimizin morfolojik yapısının temellerine kadar inilmiştir. Bu çalışma bize göstermiştir ele alınan konu oldukça zorlu bir problem olmakla birlikte Türkçe'nin yapısıda problemin çözümü konusunda işleri oldukça zor bir hale getirmektedir. 

Çalışmalarımız, literatürde de sıklıkla kullanılan Aspect Based ve Entity Based yöntemlerinin problemi gerçek manada çözmede yeterli olmayacağını göstermiştir. Bu iki yöntemi birleştirerek oluşturulacak hibrid bir yaklaşımın doğruluk için çok daha etkili olacağını göstermiştir.

Bu çıkarımda bulunduğumuz yeni bir yaklaşım, yeni bir etiketleme yöntemi ile etiketlenmiş daha fazla veriye ihtiyaç duymakla birlikte yeni ve özel bir model mimarisi ortaya koymayı da zorunlu kılmaktadır. Bundan sonra ki süreçte buradan edindiğimiz tecrübeler ışığında yüksek doğruluklu bir çözüm konusunda çalışmalar yapılacaktır.


# 🇹🇷 Acknowledgments
Bize sağladığı destek ve yenilikçi yönlendirmeleriyle Takım Danışmanımız [Dr. Duygu Çakır](https://tr.linkedin.com/in/duygu-cakir-45483164) teşekkür ederiz.
Teknofest yarışması kapsamındaki sorularımızda bizi yönlendiren ve yarışma hakkında bize güncel bilgileri sağlayan Takım Mentörümüz [Dr. Merve Ayyüce Kızrak](https://tr.linkedin.com/in/merve-ayyuce-kizrak) teşekkür ederiz.

Ayrıca takım üyelerimizin her birine ayrı ayrı [Ensar ERDOĞAN](https://tr.linkedin.com/in/ensar-erdogan-948a02161), [Oğuzhan YENEN](https://tr.linkedin.com/in/oguzhan-yenen-99a774139), [Serdar KALAYCI](https://tr.linkedin.com/in/serdar-kalayc%C4%B1-49975037) teşekkür ederiz.
