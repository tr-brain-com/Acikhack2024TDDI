## Stats


<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/1.png" height="300">
</p>

Grafiğin adı ‘Null ve Null Olamayan Değerlerin Sayısı’dır. Grafikte veri setindeki her bir sütunda ne kadar null ve null olmayan ifade olduğu gösterilmiştir. Null yeşille, null olmayan turuncuyla temsil edilmiştir. Yatay eksen veri setindeki sütunları, dikey eksense bu sütunlardaki null ve null olmayan değerlerin sayısını göstermektedir. Grafikte görüldüğü üzere çoğu sütun tamamen dolu olup null değer içermemektedir. Reason sütunu sadece null değerler içermektedir, bunun nedeni de target sütunu nötr olanların reason sütununa null değer atamamızdan ve yine bazı olumlu ve olumsuz target değeri olanların reasonlarının null olmasındandır. Bu grafik, veri setindeki eksik veri durumunu görsel olarak değerlendirmeyi sağlar ve hangi sütunlarda eksik veri olduğunu net bir şekilde gösterir. Bu tür bir analiz, veri temizleme ve hazırlama süreçlerinde oldukça faydalı olur

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/2.png" height="300">
</p>

Grafiğin adı ‘Duygu Oranı’dır. Bu grafik veri setindeki target sütununda yer alan olumlu, olumsuz ve nötr değerlerin oranlarını göstermektedir. X ekseni target sütunundaki veri isimlerini, Y ekseni ise bu değelerin oranlarını temsil eder. Grafikte en düşük oran olumluya, en yüksek oran ise olumsuza aittir. Bunun nedeni incelenen verilerin ‘şikayetvar’ ve ‘X (twitter)’ gibi yerlerden alınmış olmasıdır ve genellikle insanlar bu platformlarda şikayetlerini veya bir şey hakkındaki olumsuz düşüncelerini dile getirirler. Çubukların renkleri, her bir duygu durumunu görsel olarak ayırt etmeyi kolaylaştırır ve veri kümesinde target sütunundaki verilerin nasıl bir dağılım izlediğini açıkca ifade eder.


<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/3.png" height="300">
</p>

Bu grafiğin adı ‘Label Sütunundaki Her Değerin Sayıları’dır (0 dahil değildir). Buradaki sayılar mobil, sabit,ek paket, kampanya sütunundakilerin kombinasyonlarına karşılık gelen sayılardır. Bu sayıların hangi kombinasyonlara karşılık geldiği grafiğin sağındaki tabloda gösterilmektedir. X ekseni kombinasyonları ve Y ekseni ise bunların sayısal sıklığını ifade etmektedir. Grafikte görüldüğü gibi, "mobil" etiketi en sık gözlemlenen etikettir ve bu kategori diğerlerine göre oldukça baskındır. Çünkü mobil kullanım bir operatörün en yaygın kullanılan hizmetidir. Diğer etiketler, kombinasyonlarına bağlı olarak daha az sıklıkta gözlemlenmiştir. Bu grafik, veri setindeki etiketlerin dağılımını görsel olarak değerlendirmeyi sağlar ve hangi kombinasyonların daha sık olduğunu net bir şekilde gösterir.

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/4.png" height="300">
</p>

Bu grafik üstteki grafiğe ek olarak 0 yani mobil, sabit, ek paket, kampanyadan hiçbirinin işaretlenmemiş olduğu durumların sayısını da gösterir. 

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/5.png" height="300">
</p>

Bu grafiğin adı ‘Her Reason İçinde Severitynin Göreceli Sıklığı’dır. Bu grafik reason sütunundaki nedenlerin severity dağılımını göstermektedir. X ekseni nedenleri, Y ekseni ise severity oranlarını ifade eder. Renklerin hangi severitylere karşılık geldiği grafiğin yanındaki tabloda gösterilmiştir. Bu grafik, Turkcell'in hangi alanlarda en ciddi şikayetleri aldığını belirlemesine yardımcı olabilir ve bu alanlara odaklanarak iyileştirmeler yapmasına olanak tanır. Örnek olarak KVKK tamamen kırmızı yani burda şirketin yoğunlaşması gerekmekte, fakat boykot tamamen gri bu nedenle bu sebep göz ardı edilebilir.

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/6.png" height="300">
</p>

Bu grafiğin adı ‘Reason Sütunundaki Tüm Benzersiz Değerlerin Sayısı’dır. Grafik, reason sütunundaki benzersiz ve çeşitli nedenlerin sayısal dağılımını göstermektedir. X ekseninde nedenleri, Y ekseni ise bu nedenlerin sayısal dağılımlarını göstermektedir.. Bu grafik Turkcell’in hangi konularda en çok şikayet veya takdir aldığını net bir şekilde ortaya koymaktadır. Örneğin fatura ve network gibi nedenlerle ilgili şikayet veya övgüler en fazlayken, KVKK ve boykot gibi nedenler çok daha az şikayet veya övgü almaktadır.

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/7.png" height="300">
</p>

Bu grafiğin adı ‘Label Sütununa Göre Severity Dağılımı’dır. Grafik, mobil, sabit, ek paket ve kampanya sütunlarının kombinasyonlarından oluşan sayısal değerlere sahip satırların hangi severity değerinden kaç taneye sahip olduklarını göstermektedir. Bu grafik incelenerek hangi kombinasyonun daha ciddi olduğu anlaşılabilir. Severitylerin sıralanışı 0 1 2 şeklindedir. X ekseninde labellar y ekseninde severitylerin dağılımlarının sayısı yer almaktadır. Grafikteki renkler, şikayetlerin şiddet düzeyini temsil etmektedir. Açık renkler daha düşük şiddet düzeyini, koyu renkler ise daha yüksek şiddet düzeyini gösterir.

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/8.png" height="300">
</p>

Bu grafiğin adı ‘Aksiyonu 1 Olup Reasona Kırınımları’dır. Aksiyonun 1 olması için olumsuz olması gereklidir ama her olumsuzun aksiyonu 1 değildir. X ekseni nedenleri, Y ekseni ise onların sayılarını gösterir. Turkcell bu verileri inceleyip hangi konularda aksiyon almasının daha gerekli olduğunu anlayabilir ve hangi konularda iyi işler yaptığını anlamasını sağlayabilir. Örneğin en çok fatura ve network alanlarında frekansın yüksek olması Turkcell’i bu taraflarda çalışma yapmaya itebilir ve müşteri deneyimini iyileştirmesini sağlar.    

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/9.png" height="300">
</p>

Bu grafiğin adı ‘Reason Dağılımı’dır (Aksiyon = 1). Bu grafik aksiyonu 1 olan satırlardaki reason sütununda bulunan nedenlerin dağılımını gösterir. Turkcell bu grafiği inceleyerek hangi şikayet nedenlerinin en yaygın olduğunu ve hangilerinde aksiyon alması gerektiğini anlayabilir.



