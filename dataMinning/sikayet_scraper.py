from bs4 import BeautifulSoup
import requests
import csv

#url = 'https://www.sikayetvar.com/turkcell?page=10'
url = 'https://www.sikayetvar.com/turkcell/platinum?page=10'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://www.google.com'
}

response = requests.get(url, headers=headers)


if response.status_code == 200:
    soup = BeautifulSoup(response.content, "lxml")

    # Şikayet detaylarını içeren tüm div elementlerini bulun
    basliklar = soup.find_all("article", attrs={"class":"card-v2 ga-v ga-c"})

    # CSV dosyası oluşturma
    with open('turkcell-platinum/sikayet_turkcell-platinum_page10.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='|')
        writer.writerow(["Link", "Content"])  # Başlık satırı

        for baslik in basliklar:
            link = baslik.find("h2", attrs={"class": "complaint-title"})
            link_devam = link.a.get("href")
            link_basi = "https://www.sikayetvar.com"
            link_total = link_basi + link_devam
            print(link_total)

            detay = requests.get(link_total, headers=headers)
            detay_soup = BeautifulSoup(detay.content, "lxml")

            teknik_ayrintilar = detay_soup.find_all("div", attrs={"class":"complaint-detail-description"})

            for i in teknik_ayrintilar:
                content = i.text.strip()
                # Link ve content'i CSV dosyasına yaz
                writer.writerow([link_total, content])
else:
    print("Web sitesine erişim sağlanamadı, hata kodu:", response.status_code)













