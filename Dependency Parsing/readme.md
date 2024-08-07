## Dependency Parsing ##

Bu bölüm, problem tanımı uyarınca cümle içerisinde geçen farklı varlıklara yönelik duyguları tespit etmek amacıyla geliştirilmiştir. Yapılan araştırmalar ve gerçekleştirilen çalışmalar incelendiğinde problem çözümüne yönelik olarak <b>Aspect Based</b> ve <b>Entity Based</b> olarak iki farklı yöntem geliştirildiği; bu yöntemlerin  seçimi konusunda da alana özgü verilerin yapısının etkili olduğu fark edilmiştir.<br>

<b>Aspect Based</b>, bir cümlede veya belgede belirtilen belirli yönlerle ilişkili duyguyu belirleme görevini ifade eder. <br>

<b>Entity Based</b> olarak ifade edilen yapı ise cümle içinde belirlenen varlıklara yönelen duyguların tespitini sağlamayı ifade eder.<br>

Bu çalışma için ürettiğimiz, geliştirdiğimiz veri (ayrıntılı bilgi stats içerisinde mevcuttur), hem entity hemde aspect tabanlı hibrid bir yapının ortaya konulmasını bizim için gerekli kılmıştır. Bu noktada <b>Dependency Parsing</b> olarak bilinen bir dile ait cümle yapılarının detaylı şekilde incelenmesi ve yorumlanması gerekmiştir. Dependency parsing ile  cümle bölümlendirmesi ve entity tabanlı ayrıştırma birlikte öğrenilir. Mevcut problemde entity bazlı duyguları veya entity yönelik duyguları tespit etmek amacıyla SpaCy kullanarak kural tabanlı  bir yapı inşa edilmiştir. Bu kural tabanlı yapı, metinlerin standart cümle yapısına uymayacağı (twitter verileri gb. ) fikrinden hareketle ortaya çıkarılmış, metin içerisinde ki varlıklara yönelen duyguların tespitinde oldukça başarılı sonuçlar elde edilmiştir.<br>

Spacy dilbilimsel olarak hazır bileşenler içeren metin sınıflandırma, etikete bağlı dayalı bağımlılıkları analiz etme, cümleleri bölme, morfolojik analiz ve kök ayırma gibi bir çok problemin çözümünde kullanılan bir kütüphanedir. Türkçe için cümledeki kelimelerin bağımlıklarını bulmak için tr_core_web_trf adında daha önce eğitilmiş, tranformer tabanlı pipeline model kullanıldı. CNN-tabanlı diğer modellerden tr_core_web_lg, tr_core_web_md gibi modellere göre daha yüksek doğruluk sunduğu için tercih edildi. Model herkese açık bir şekilde erişilebilir ve linkten ulaşılabilir durumdadır.<br>https://github.com/turkish-nlp-suite/turkish-spacy-models

Bağlılık Ayrıştırması(Dependency Parsing) ile hedefimiz bir cümle içerisindeki, sözcükler arasındaki ilişkileri ve ilişki türlerini belirleyerek ilgili cümlenin çözümlemesini sağladığından cümledeki kelime öbeklerini çıkarmada bize yol gösterici olacaktır. Örneğin "tt çekmiyor vodafone hizmeti rezalet ötesi kesinti oluyor. Turkcell fiyat farkını hak ediyor." cümlesini ele alacak olursak 

<p align="center">
  <img alt="Dependency Parsing Uygulanmış Örnek Bir Cümle" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/dependency_parsing_01.png" height="300">
</p>
