#  🇹🇷 Acikhack2024TDDI
Teknofest 2024 Türkçe Doğal Dil işleme Senaryo Kategorisi

Bu kısma real time uygulama gif eklenebilir

#  🇹🇷 Data Minning
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/beautifulsoup.jpg" height="300">
</p>
Veri madenciliği, büyük veri setlerinden anlamlı ifadeler, ilişkiler ve bilgiler çıkarmak için kullanılan bir süreçtir. Veri madenciliği, veri hazırlama, model oluşturma, değerlendirme ve sonuçları yorumlama gibi adımları içerir.
BeautifulSoup ve Scrapy: Web kazıma (web scraping) için kullanılır. İnternetten veri çekmek ve analiz etmek için kullanışlıdır. BeautifulSoup, Python'da HTML ve XML dosyalarını ayrıştırmak ve analiz etmek için ,
kullanılan bir kütüphanedir. Web sayfalarından veri çekmek, web kazıma (web scraping) işlemlerinde sıklıkla tercih edilir. HTML ve XML dosyalarını kolayca ayrıştırır.Belgelerdeki elementlere, etiketlere ve niteliklere hızlı ve kolay erişim sağlar.
Belgeleri ağaç yapısı (parse tree) olarak temsil eder ve bu sayede belirli elementleri seçip işlemek kolaylaşır.

2024 Teknofest Türkçe Dogal Dil İşleme kategorisi için data minning code blogunu adım adım incelemek için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/edit/main/dataMinning/Readme.md).

#  🇹🇷 Data Stats
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-07-30%2008-46-02.png" height="300">
</p>

Teknofest yarışması kapsamında,X platformu, Şikayet web sayfası ve Yıldız Teknik Üniversitesi'nin duygu analizi çalışmasından elde edilen veri setleri birleştirilerek toplamda 20,700 veri noktası içeren kapsamlı bir veri seti oluşturulmuştur. Bu veri seti, çeşitli ürünler ve hizmetlerle ilgili kullanıcı geri bildirimlerini ve şikayetleri kapsamaktadır.

Veri Dağılımı:

    Olumsuz İfadeler: %60
    Nötr İfadeler: %20
    Olumlu İfadeler: %20


Veri setinin genel eğilimlerini ve kullanıcıların duygusal tepkilerini anlamak için önemli bir başlangıç noktasıdır. Bu veriler, gelecekteki hizmet iyileştirmeleri, müşteri deneyimini geliştirme stratejileri ve pazarlama kampanyaları için değerli içgörüler sağlayabilir. 

Veriseti analiz [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/stats/readme.md).



# 🇹🇷 Data Cleanning
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/cleaning.png" height="300">
</p>
Cleaning service, bu çalışmaya uygun olarak yapılan denemeler sonucunda bir standart belirlenerek çoğu bölümü opsiyonel olarak kullanılabilecek şekilde geliştirilmiştir. 

Temizleme servisi hakkında daha ayrıntılı bilgi almak ve detaylar için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/cleaning-service/readme.md).


# 🇹🇷 Named Entity Recognition

2024 Teknofest Doğal Dil İşleme (NLP) senaryo kategorisinde, Türkcell gibi mobil operatörler ve bunlarla ilişkili olan ürünler, paketler ve uygulamaları (Superonline, Platinum Paket, BİP, Fizy, Lifebox, Müşteri Hizmetleri vb.) kapsayan, metinler içinden ilgili varlıkları çıkarmak amacıyla geliştirilmiş olan projedir.

Geliştirilen model için veriler X platformundan üzerinden @Turkcell varlığına ilişkin yapılan yorumlar toplanarak ve sikayetvar web sayfası üzerinden yapılan scrabing ile veri alınması süreçleri ile temin edilmiştir. Elde edilen 20700 adet veri, açık kaynak Doccano uygulaması ile etiketlenmiş; bu etiketleme işleminde daha detaylı analiz yapılmasını sağlayabilmek adına etiketler, <b><u>"OPERATOR, URUN, HIZMET, UYGULAMA ve PAKET"</u></b> gibi başlıklara ayrılmıştır.


Tüm bu süreçler sonucunda elde edilen veri dosyası "ner-service/data/dataset.conll" adresinde bulunmaktadır. Son durumda tag ve örnek sayıları aşağıdaki gibi oluşmuştur.

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


NER (Varlık İsmi Çıkarımı) aşamasını adım adım incelemek için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/tree/main/ner-service).

# 🇹🇷 Sentiment Analysis

Veri seti elde ettiğimiz kaynaklar için Stats kısmında ayrıca anlatılmaktadır. Ayrıntılı bilgi için Stats kısmını tıklayınız.

BERT tabanlı bir model kullanarak Türkçe metinlerde duygu analizi yapmaktadır. Proje kapsamında k-fold çapraz doğrulama yöntemi uygulanmıştır."bert-base-turkish-cased" modeli, Türkçe dilinde büyük ve küçük harf ayrımını dikkate alır. Bu, dil bilgisi ve kelime anlamları açısından önemli olabilir. Cased model kullanmak, özellikle özel isimlerin doğru şekilde anlaşılması ve sınıflandırılması açısından avantaj sağlar.

Her modelimiz ayrı ayrı rest servis olcak şekliyle hazırlanmıştır. Model başarı değerleri aşağıdaki gibidir. 
| Sınıf        | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| 0  (Nötr)          | 0.766     | 0.764  | 0.765    | 577     |
| 1  (Olumlu)          | 0.757     | 0.790  | 0.773    | 352     |
| 2  (0lumsuz)          | 0.920     | 0.910  | 0.915    | 1305    |
| **Accuracy** | |        |        **0.854**   | **2234**|
| **Macro Avg**| **0.814** | **0.821** | **0.818** | **2234** |
| **Weighted Avg** | **0.855** | **0.854** | **0.854** | **2234** |

Model training ve Rest Api kodları için ayrıntılı açıklaması için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/Sentiment%20Analysis/readme.md).

# 🇹🇷 Severity Classification
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-08-02%2021-03-13.png" height="600">
</p>

2024 Teknofest Doğal Dil İşleme (NLP) senaryo kategorisinde, Türkcell ve ürünleri (Superonline, Platinum Paket, BİP, Fizy, Lifebox vb.) hakkında kullanıcı yorumlarına dayalı özgün bir entity bazlı duygu analizi gerçekleştirilmiştir. Bu çalışmada, yalnızca yorumların duygusal tonu belirlenmemiş, aynı zamanda yorumların taşıdığı önem veya aciliyet düzeyini belirtmek için "severity" adı verilen ekstra bir kategori de eklenmiştir. "Severity" kolonu, metinde tartışılan konunun aciliyet veya önem derecesini ifade eder; 0 önemsiz, 1 orta derecede önemli ve 2 acil bir durumu belirtir. Ayrıntılı bilgi ve kod için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/severity%20Classification/readme.md).

# 🇹🇷 Reason Classification
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-08-02%2021-21-59.png" height="600">
</p>

Teknofest 2024'teki Doğal Dil İşleme (NLP) senaryo kategorisi yarışmasında katıldığımız proje, entity bazlı duygu analizi üzerine odaklanmaktadır. Projemizde, Turkcell ve ürünleri hakkında yazılan metinlerde olumsuzluğa sebep olan kategorilerin tespitini amaçlayarak özgünlük sağlamak için veri setine "reason" (sebep) kolonu eklenmiştir. Bu kolon, kullanıcıların olumsuz duygu bildirdiği durumlarda hangi kategoriye (örneğin bayi, fatura, kampanya) dair olumsuzluk yaşadıklarını belirlememize olanak tanımaktadır.Ayrıntılı bilgi ve kod için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/reason%20classificaiton/readme.md).


# 🇹🇷 Application

#  🇹🇷 Contribution
2024 Teknofest Türkçe Doğal Dil İşleme senaryo kategorisi yarışmasında, projemiz varlık tabanlı duygu analizine odaklanmaktadır. Bu kapsamda, X ve Şikayet Var sayfalarından veri madenciliği yaparak kendi verilerimizi oluşturduk. Yarışmanın ana hedefi, metin içerisindeki varlıkları tespit etmek ve bu varlıklara ait duygu analizini yaparak sonuçları olumlu, olumsuz ve nötr olarak sınıflandırmaktır. Analizimizin kapsamını ve derinliğini artırmak için veri setimize ek kolonlar ekledik ve her biri aşağıda açıklanmaktadır


| Category       | Description                                                              
| ----------     | ---------------------------------------------
| Entity Listesi          | Metinde geçen varlıkların listesini içerir. Yaklaşık 100 farklı varlık tespit ettik, böylece analizimizin geniş bir kapsama sahip olmasını sağladık.
| Target      | Tespit edilen varlıkla ilişkili duygu burada olumlu, olumsuz veya nötr olarak sınıflandırılır. Bu, yarışmanın gereksinimlerine uygun olarak belirlenmiştir.       
| Severity         | Metinde tartışılan konunun aciliyet veya önem derecesini belirtir. 0 önemsiz, 1 orta derecede önemli ve 2 acil bir durumu ifade eder           
| Reason         | Olumsuz duygular için belirlenmiştir, sorunun kaynağını belirler. Örneğin, fatura, ağ (network) sorunları, mobil numara taşıma (mnp) gibi. Bu, müşteri memnuniyetsizliğinin temel nedenini anlamamıza yardımcı olur    
| Muhatap         | Türkcel'in muhatap olup olmadığını belirtir.     
| Mobil         | Sorunun mobil hat ile ilgili olup olmadığını belirtir      
| Sabit         | Sorunun sabit hat ile ilgili olup olmadığını belirtir.      
| Ek Paket         |  Sorunun ek paketlerden kaynaklanıp kaynaklanmadığını belirtir.   
|Kampanya        |   Sorunun bir kampanyadan (örneğin, promosyon teklifleri, ekstra GB) kaynaklanıp kaynaklanmadığını belirtir.
| Diğer Ürün/Uygulama         |  Türkcel'in hangi uygulama veya ürününden (örneğin, BIP, Fizy, Platinum) kaynaklandığını belirler.   
| Reklam         |  Türkcel'in reklamları, sponsorlukları veya boykotları ile ilgili şikayetleri kaydeder.      
| Çağrı Merkezi         |Çağrı merkezi ve teknik destek ile ilgili şikayetleri bu kolonda belirtilir.     
| Bayi         |      Satış noktaları ve mağazalarla ilgili şikayetleri kaydeder.
| Aksiyon       |  Aciliyet seviyesi 1 veya 2 olan durumlar için belirlenir, aksiyon alınıp alınmayacağını belirler. 0 aksiyon alınmayacağını, 1 ise müdahale edilmesi gerektiğini ifade eder.    

Bu ek kolonlar sayesinde, daha ayrıntılı ve eyleme geçirilebilir bir duygu analizi sunmayı amaçlıyoruz. Yaklaşımımız, yarışmanın gereksinimlerini karşılamakla kalmayıp, aynı zamanda Türkcel'in müşteri şikayetlerine daha etkili bir şekilde yanıt vermesine ve genel müşteri memnuniyetini ve hizmet kalitesini artırmasına yardımcı olabilecek değerli içgörüler sunmaktadır. Bu geliştirilmiş veri seti yapısı, müşteri geri bildirimlerinin daha derinlemesine anlaşılmasını sağlar ve hedefe yönelik müdahaleler ile stratejik karar alma süreçlerini destekler.
# 🇹🇷 Results

# 🇹🇷 Acknowledgments
Bize sağladığı destek ve yenilikçi yönlendirmeleriyle Takım Danışmanımız [Dr. Duygu Çakır](https://tr.linkedin.com/in/duygu-cakir-45483164) teşekkür ederiz.
Teknofest yarışması kapsamındaki sorularımızda bizi yönlendiren ve yarışma hakkında bize güncel bilgileri sağlayan Takım Mentörümüz [Dr. Merve Ayyüce Kızrak](https://tr.linkedin.com/in/merve-ayyuce-kizrak) teşekkür ederiz.

Ayrıca takım üyelerimizin her birine ayrı ayrı [Ensar ERDOĞAN](https://tr.linkedin.com/in/ensar-erdogan-948a02161), [Oğuzhan YENEN](https://tr.linkedin.com/in/oguzhan-yenen-99a774139), [Serdar KALAYCI](https://tr.linkedin.com/in/serdar-kalayc%C4%B1-49975037) teşekkür ederiz.
