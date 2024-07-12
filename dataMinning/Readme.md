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
