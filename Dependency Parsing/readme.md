## Dependency Parsing ##

Bu bölüm, problem tanımı uyarınca cümle içerisinde geçen farklı varlıklara yönelik duyguları tespit etmek amacıyla geliştirilmiştir. Yapılan araştırmalar ve gerçekleştirilen çalışmalar incelendiğinde problem çözümüne yönelik olarak <b>Aspect Based</b> ve <b>Entity Based</b> olarak iki farklı yöntem geliştirildiği; bu yöntemlerin  seçimi konusunda da alana özgü verilerin yapısının etkili olduğu fark edilmiştir.<br>

<b>Aspect Based</b>, bir cümlede veya belgede belirtilen belirli yönlerle ilişkili duyguyu belirleme görevini ifade eder. <br>

<b>Entity Based</b> olarak ifade edilen yapı ise cümle içinde belirlenen varlıklara yönelen duyguların tespitini sağlamayı ifade eder.<br>

Bu çalışma için ürettiğimiz, geliştirdiğimiz veri (ayrıntılı bilgi stats içerisinde mevcuttur), hem entity hemde aspect tabanlı hibrid bir yapının ortaya konulmasını bizim için gerekli kılmıştır. Bu noktada <b>Dependency Parsing</b> olarak bilinen bir dile ait cümle yapılarının detaylı şekilde incelenmesi ve yorumlanması gerekmiştir. Dependency parsing ile  cümle bölümlendirmesi ve entity tabanlı ayrıştırma birlikte öğrenilir. Mevcut problemde entity bazlı duyguları veya entity yönelik duyguları tespit etmek amacıyla SpaCy kullanarak kural tabanlı  bir yapı inşa edilmiştir. Bu kural tabanlı yapı, metinlerin standart cümle yapısına uymayacağı (twitter verileri gb. ) fikrinden hareketle ortaya çıkarılmış, metin içerisinde ki varlıklara yönelen duyguların tespitinde oldukça başarılı sonuçlar elde edilmiştir.<br>
