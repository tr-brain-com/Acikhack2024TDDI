## Data Minning

Veri madenciliği, büyük veri kümelerinden anlamlı ifadeler, ilişkiler ve bilgiler çıkarmak için kullanılan bir süreçtir. Veri madenciliği, veri hazırlama, model oluşturma, değerlendirme ve sonuçları yorumlama gibi adımları içerir.
BeautifulSoup ve Scrapy: Web kazıma (web scraping) için kullanılır. İnternetten veri çekmek ve analiz etmek için kullanışlıdır. BeautifulSoup, Python'da HTML ve XML dosyalarını ayrıştırmak ve analiz etmek için ,
kullanılan bir kütüphanedir. Web sayfalarından veri çekmek, web kazıma (web scraping) işlemlerinde sıklıkla tercih edilir.HTML ve XML dosyalarını kolayca ayrıştırır.Belgelerdeki elementlere, etiketlere ve niteliklere hızlı ve kolay erişim sağlar.
Belgeleri ağaç yapısı (parse tree) olarak temsil eder ve bu sayede belirli elementleri seçip işlemek kolaylaşır.Kurulum aşağıdaki gibidir.
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
İnternet sitesinden verilerin çekileceği URL'yi belirtiyoruz. Bu URL, Turkcell Platinum şikayetlerinin 10. sayfasını temsil eder.
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

