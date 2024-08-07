## Data Minning

Veri madenciliği, büyük veri kümelerinden anlamlı ifadeler, ilişkiler ve bilgiler çıkarmak için kullanılan bir süreçtir. Veri madenciliği, veri hazırlama, model oluşturma, değerlendirme ve sonuçları yorumlama gibi adımları içerir.
BeautifulSoup ve Scrapy: Web kazıma (web scraping) için kullanılır. İnternetten veri çekmek ve analiz etmek için kullanışlıdır. BeautifulSoup, Python'da HTML ve XML dosyalarını ayrıştırmak ve analiz etmek için ,
kullanılan bir kütüphanedir. Web sayfalarından veri çekmek, web kazıma (web scraping) işlemlerinde sıklıkla tercih edilir. HTML ve XML dosyalarını kolayca ayrıştırır. Belgelerdeki elemanlara, etiketlere ve niteliklere hızlı ve kolay erişim sağlar.
Belgeleri ağaç yapısı (parse tree) olarak temsil eder ve bu sayede belirli elementleri seçip işlemek kolaylaşır. Kurulum aşağıdaki gibidir.
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p>pip install beautifulsoup4 </p>
</body>
</html>
</code></pre>

BeautifulSoup ve requests kütüphanelerini import ediyoruz. BeautifulSoup, HTML ve XML dosyalarını ayrıştırmak için kullanılırken, requests, HTTP istekleri yapmak için kullanılır. csv kütüphanesi ise CSV dosyalarıyla çalışmak için kullanılır.
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p>from bs4 import BeautifulSoup
import requests
import csv</p>
</body>
</html>
</code></pre>
İnternet sitesinden verilerin çekileceği adresi (URL) belirtiyoruz. Bu URL, Turkcell Platinum şikayetlerinin 10. sayfasını temsil eder.
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p>url = 'https://www.sikayetvar.com/turkcell/platinum?page=10'</p>
</body>
</html>
</code></pre>
HTTP isteklerinde kullanılacak başlıkları (headers) tanımlıyoruz. Bu başlıklar, tarayıcıdan geliyormuş gibi görünmesini sağlar ve bazen erişim izni almayı kolaylaştırır.
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p>headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.google.com'
}</p>
</body>
</html>
</code></pre>
Belirtilen URL'ye HTTP GET isteği gönderiyoruz ve yanıtı (response) alıyoruz.Eğer HTTP isteği başarılı (status code 200) ise, gelen HTML içeriğini BeautifulSoup ile ayrıştırıyoruz. "lxml" ayrıştırıcıyı kullanıyoruz.
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p> response = requests.get(url, headers=headers)
    if response.status_code == 200:
    soup = BeautifulSoup(response.content, "lxml")</p>
</body>
</html>
</code></pre>
HTML içeriğinde, şikayet detaylarını içeren tüm article elementlerini class attributeleri "card-v2 ga-v ga-c" olanları buluyoruz. Belirtilen dosya yolunda yeni bir CSV dosyası oluşturuyoruz. Dosya yazma modunda (mode='w') açılıyor ve UTF-8 karakter kodlaması kullanılıyor. CSV dosyasına yazmak için bir csv.writer oluşturuyoruz ve dosyaya "Link" ve "Content" başlıklarını içeren ilk satırı yazıyoruz.
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p>  basliklar = soup.find_all("article", attrs={"class":"card-v2 ga-v ga-c"})
  with open('turkcell-platinum/sikayet_turkcell-platinum_page10.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(["Link", "Content"])  # Başlık satırı
    </p>
</body>
</html>
</code></pre>
Bulunan her article elemanında şikayet başlığını içeren h2 elemanını buluyoruz. Bu h2 elemanı içindeki a etiketiyle şikayetin detaylarına giden bağlantıyı alıyoruz ve tam URL'yi oluşturuyoruz (link_basi ile link_devam'ı birleştirerek).
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p>   for baslik in basliklar:
            link = baslik.find("h2", attrs={"class": "complaint-title"})
            link_devam = link.a.get("href")
            link_basi = "https://www.sikayetvar.com"
            link_total = link_basi + link_devam
            print(link_total)
    detay = requests.get(link_total, headers=headers)
    detay_soup = BeautifulSoup(detay.content, "lxml")
    </p>
</body>
</html>
</code></pre>
Detay sayfasına bir HTTP GET isteği gönderiyoruz ve gelen içeriği BeautifulSoup ile ayrıştırıyoruz. Detay sayfasında, şikayet detaylarını içeren div elemanlarından sınıf (class) nitelikleri (attribute) "complaint-detail-description" olanları buluyoruz.
<pre><code>
<!DOCTYPE html>
<html>
<body>
    <p>  teknik_ayrintilar = detay_soup.find_all("div", attrs={"class":"complaint-detail-description"})
    for i in teknik_ayrintilar:
            content = i.text.strip()
            writer.writerow([link_total, content])
    </p>
</body>
</html>
</code></pre>


