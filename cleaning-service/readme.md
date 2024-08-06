
## Brain-Cleaning-Service
Doğal Dil İşleme teknolojisi, hammadde olarak metinleri kullanır. Bu sebeple doğal dil işleme görevlerinde verileri temizleme veya veri üzerinde bazı önişleme adımlarını uygulama model oluşturma kadar önemli bir adımdır. Bu çalışma, özellikle yapılandırılmamış veriler üzerinde daha doğru sonuçlar elde edilmesi açısından "cleaning" işlemini moduler olarak sunmayı amaçlamaktadır.

Metinsel verilerimiz olduğunda, kelimeleri makine öğrenme algoritmalarıyla çalışan sayısal özelliklere dönüştürmek için verilere birkaç ön işleme adımı uygulamamız gerekir. Bir problem için ön işleme adımları, esas olarak etki alanına ve problemin kendisine bağlıdır, bu nedenle, tüm adımları her probleme uygulamamız gerekmez. 

Bu çalışmada metin içerisinden anlam ifade edecek her türlü veriyi tutarak veri üzerinde önişleme yapmak amaçlanmaktadır. Bu kapsam kodlar parametrik olarak geliştirilerek farklı durumlarda senaryoların test edilmesine uygun hale getirilmiştir.

## Servis Mimarisi
Çalışma, micro servis mimarisi üzerine inşa edilmiştir. FastAPI çerçevesi kullanılmıştır. FastAPI, standart Python tipi ipuçlarına dayalı Python 3.9+ ile API'ler oluşturmaya yönelik modern, hızlı (yüksek performanslı) bir web çerçevesidir.

Çalıştırmak için,

**uvicorn api.main:app --reload --port 9090**

## Servisin Yapısı
Servis **"clean"** endpointi ile hizmet verecek şekilde tasarlanmıştır. Girdi olarak kendine üç adet parametre alır. Bunlar:

text: [str] Default ""
constraction: [bool] Default True
opword: [bool] Default 

Bu parametreler de text haric diğer parametreler opsiyoneldir. Text parametresi clean edilecek ham metin bilgisini göstermektedir. Constraction parametresi bu çalışmada ki problemin çözümüne yönelik olarak geliştirilmiştir. Kısaltmaları gerçek kelimelere dönüştürür. Örneğin "g*t" kelimesini "göt" olarak çevirmek. Bu işlemin model başarımını etkilediği fark edildi. Bu sebeble clean işlemine eklendi.

## Temizleme (Clean) İşlemi

Geliştirilen clean sınıfının clean metodu aşağıdaki gibidir.

clean metodu:

```python

        def clean(self):
        temp_text = self.Text
        temp_text = self.lowercase(temp_text)
        temp_text = self.split(temp_text)

        if self.Contractions: #Kısaltmaları dönüştür
            new_text = []
            for word in temp_text:
                if word in self.Contractions_List:
                    new_text.append(self.Contractions_List[word])
                else:
                    new_text.append(word)
            temp_text = " ".join(new_text)

        temp_text = self.tweet_tag_clean(temp_text) #tweet ve tag temizle
        temp_text = self.http_clean(temp_text) #http tag temizle
        temp_text = self.numeric_clean(temp_text) #numeric değerleri temizle
        temp_text = self.special_character_clean(temp_text)  #special karakterleri temizle

        if self.StopWords:
            temp_text = self.stopwords_clean(temp_text)  #stopword kelimeleri temizle

        temp_text = self.single_characters_clean(temp_text)  # special karakterleri ve emojileri temizle

        temp_text = temp_text.lstrip().rstrip()  #text baş ve sonundaki boşlukları at

        return temp_text

```


Temizleme işleminde uygulanan adımlar şu şekildedir:

- ***Metni küçük harfe dönüştürme*** : ***Standart***
- ***Metni tokenize etmek*** : Metni kelime kelime ayırma. ***Standart***
- ***Tag temizleme*** : Genel olarak sosyal medya verileri kullanıldığından hareketle @ ve # gibi ifadelerle başlayan kelimelerin kaldırılmasına yöneliktir. ***Standart***
- ***Html ve url bilgilerinin kaldırılması*** : Metnin anlam bütünlüğü üzerinde bir etkisi olmadığından metinden çıkarılmasına yöneliktir. ***Standart***
- ***Numeric ifadelerin kaldırılması*** : Metin önişleme adımlarında standart olarak kullanılan numeric ifadelerin temizlenmesine yöneliktir. ***Standart***
- ***Özel karakterlerin kaldırılması*** : Metin içerisinde anlamı bozmayan fakat başarımı olumsuz etkileyen noktalama işaretleri ve her türlü ifadelerin kaldırılması. ***Standart***
- ***Stopwords karakterlerin kaldırılması*** : Stopwords karakterleri, herhangi bir ek kütüphane kullanmadan kendi oluşturduğumuz bir sözlüğe göre temizlenmektedir. Liste 440 adet kelimeden oluşmaktadır. Başarımı direk etkilediğindne devre dışı bırakılabilecek şekilde hazırlanmıştır. ***Opsiyonel***
- ***Tek karakterlerin temizlenmesi*** : Farklı dillerde bir anlam ifade etsede türkçe tek karakter uzunluğunda ki kelimelerin bir anlamı olmadığından bunlarında kaldırılmasına yöneliktir. ***Standart***
- ***Kısaltmaların dönüştürülmesi*** : Özellikle sosyal medya platformalarında aşağılayıcı ve küfür içeren ifadeler kısaltmalar şeklinde ve farklı farklı olabilmektedir. Bu sebeble bunlara bir standart getirmek amacıyla oluşturulmuştur. Şöyleki "b*k", "g.t" gibi ifadeler orjinal kelimelerinden farklı oldukları için bunları yakalamak adına bir dönültürme işleminin başarıyı arttıracağı düşünülmüştür ve bu amaçla geliştirilmiştir. ***Opsiyonel***
- ***Kelimelerin düzeltilmesi (spell correction)*** : Bu işlem, bu çalışmaya konu olan veri setinin sosyal medyada kullanılan kullanıcı mesajlarını içerdiği için eklenmiştir. Çünkü sosyal medyada kullanılan kelimeler özensiz, düzensiz ve gerçek yazımından farklı olabilmektedir. Bu sebeblerden dolayı metinde geçen kelimelere bir standart getirmek, kelimelerin gerçek yazımını elde etmek, eğitim ve tahmin aşamasına da bir standart getirmiş oldu ve bu durum ayrıca model performansını da olumlu şekilde etkiledi.***Standart***

  ## Sonuçlar

Bilindiği üzere doğal dil işleme problemlerinde metin üzerinde yapılan önişleme adımları büyük önem arzetmektedir. Bu çalışmada önişleme adımları geliştirilirken göz önüne aldığımız en önemli nokta, her adımın model başarımını ve performansını nasıl etkilediği üzerine olmuştur. Burada geliştirilen model, bu çalışma kapsamında en etkili olan ön işlem adımlarının bütününden oluşmaktadır. 
