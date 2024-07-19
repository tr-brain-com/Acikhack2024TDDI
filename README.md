#  🇹🇷 Acikhack2024TDDI
Teknofest 2024 Türkçe Doğal Dil işleme Senaryo kategorisi

BU kısma real time uygulama gif eklenebilir

#  🇹🇷 Data Minning
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/beautifulsoup.jpg" height="300">
</p>
Veri madenciliği, büyük veri kümelerinden anlamlı ifadeler, ilişkiler ve bilgiler çıkarmak için kullanılan bir süreçtir. Veri madenciliği, veri hazırlama, model oluşturma, değerlendirme ve sonuçları yorumlama gibi adımları içerir.
BeautifulSoup ve Scrapy: Web kazıma (web scraping) için kullanılır. İnternetten veri çekmek ve analiz etmek için kullanışlıdır. BeautifulSoup, Python'da HTML ve XML dosyalarını ayrıştırmak ve analiz etmek için ,
kullanılan bir kütüphanedir. Web sayfalarından veri çekmek, web kazıma (web scraping) işlemlerinde sıklıkla tercih edilir.HTML ve XML dosyalarını kolayca ayrıştırır.Belgelerdeki elementlere, etiketlere ve niteliklere hızlı ve kolay erişim sağlar.
Belgeleri ağaç yapısı (parse tree) olarak temsil eder ve bu sayede belirli elementleri seçip işlemek kolaylaşır.

2024 Teknofest Türkçe Dogal Dil İşleme kategorisi için data minning code blogunu adım adım incelemek için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/edit/main/dataMinning/Readme.md).

#  🇹🇷 Data Stats
Veri seti istatistikleri

#  🇹🇷 Exploratory Data Analysis
Veri seti içerisinde analiz çalışması

# 🇹🇷 Data Preparation

# 🇹🇷 Data Cleanning
<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/cleaning.png" height="300">
</p>
Cleaning service, bu çalışmaya uygun olarak yapılan denemeler sonucunda bir standart belirlenerek çoğu bölümü opsiyonel olarak kullanılabilecek şekilde geliştirilmiştir. Temizleme servisi hakkında daha ayrıntılı bilgi almak ve detaylar için [tıklayınız](https://github.com/tr-brain-com/Acikhack2024TDDI/tree/main/cleaning-service/readme.md).

#  🇹🇷 Contribution
2024 Teknofest Türkçe Doğal Dil İşleme senaryo kategorisi yarışmasında, projemiz varlık tabanlı duygu analizine odaklanmaktadır. Bu kapsamda, X ve Şikayet Var sayfalarından veri madenciliği yaparak kendi verilerimizi oluşturduk. Yarışmanın ana hedefi, metin içerisindeki varlıkları tespit etmek ve bu varlıklara ait duygu analizini yaparak sonuçları olumlu, olumsuz ve nötr olarak sınıflandırmaktır. Analizimizin kapsamını ve derinliğini artırmak için veri setimize ek kolonlar ekledik ve her biri aşağıda açıklanmaktadır:

    Entity Listesi: Metinde geçen varlıkların listesini içerir. Yaklaşık 100 farklı varlık tespit ettik, böylece analizimizin geniş bir kapsama sahip olmasını sağladık.

    Target: Tespit edilen varlıkla ilişkili duygu burada olumlu, olumsuz veya nötr olarak sınıflandırılır. Bu, yarışmanın gereksinimlerine uygun olarak belirlenmiştir.

    Severity: Metinde tartışılan konunun aciliyet veya önem derecesini belirtir. 0 önemsiz, 1 orta derecede önemli ve 2 acil bir durumu ifade eder.

    Reason: Olumsuz duygular için belirlenmiştir, sorunun kaynağını belirler. Örneğin, fatura, ağ (network) sorunları, mobil numara taşıma (mnp) gibi. Bu, müşteri memnuniyetsizliğinin temel nedenini anlamamıza yardımcı olur.

    Muhattap: Türkcel'in muhatap olup olmadığını belirtir.

    Mobil: Sorunun mobil hat ile ilgili olup olmadığını belirtir.

    Sabit: Sorunun sabit hat ile ilgili olup olmadığını belirtir.

    Ek Paket: Sorunun ek paketlerden kaynaklanıp kaynaklanmadığını belirtir.

    Kampanya: Sorunun bir kampanyadan (örneğin, promosyon teklifleri, ekstra GB) kaynaklanıp kaynaklanmadığını belirtir.

    Diğer Ürün/Uygulama: Türkcel'in hangi uygulama veya ürününden (örneğin, BIP, Fizy, Platinum) kaynaklandığını belirler.

    Reklam: Türkcel'in reklamları, sponsorlukları veya boykotları ile ilgili şikayetleri kaydeder.

    Çağrı Merkezi: Çağrı merkezi ve teknik destek ile ilgili şikayetleri bu kolonda toplar.

    Bayi: Satış noktaları ve mağazalarla ilgili şikayetleri kaydeder.

    Aksiyon: Aciliyet seviyesi 1 veya 2 olan durumlar için belirlenir, aksiyon alınıp alınmayacağını belirler. 0 aksiyon alınmayacağını, 1 ise müdahale edilmesi gerektiğini ifade eder.

Bu ek kolonlar sayesinde, daha ayrıntılı ve eyleme geçirilebilir bir duygu analizi sunmayı amaçlıyoruz. Yaklaşımımız, yarışmanın gereksinimlerini karşılamakla kalmayıp, aynı zamanda Türkcel'in müşteri şikayetlerine daha etkili bir şekilde yanıt vermesine ve genel müşteri memnuniyetini ve hizmet kalitesini artırmasına yardımcı olabilecek değerli içgörüler sunmaktadır. Bu geliştirilmiş veri seti yapısı, müşteri geri bildirimlerinin daha derinlemesine anlaşılmasını sağlar ve hedefe yönelik müdahaleler ile stratejik karar alma süreçlerini destekler.

# 🇹🇷 Named Entitiy Recognation

# 🇹🇷 Sentiment Analysis

# 🇹🇷 Model usage

# 🇹🇷 Application

# 🇹🇷 Results

# 🇹🇷 Acknowledgments
Bize sağladığı destek ve yenilikçi yönlendirmeleri için  Takım Danışmanımız [DR.Duygu Çakır](https://tr.linkedin.com/in/duygu-cakir-45483164) teşekkür ederiz.
Teknofest yarışması kapsamında bizi her türlü sorularımızda yönlendiren yarışma durumları hakkında sürekli güncel bilgiler sağlayan Takım Mentörümüz [DR.Merve Ayyüce Kızrak](https://tr.linkedin.com/in/merve-ayyuce-kizrak) teşekkür ederiz.

Ayrıca takım üyelerimizin her birine ayrı ayrı [Ensar ERDOĞAN](https://tr.linkedin.com/in/ensar-erdogan-948a02161), [Oğuzhan YENEN](https://tr.linkedin.com/in/o%C4%9Fuzhan-yenen-99a774139), [Serdar KALAYCI](https://tr.linkedin.com/in/serdar-kalayc%C4%B1-49975037) teşekkür ederiz.
