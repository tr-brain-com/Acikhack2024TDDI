## Severity Classification
2024 Teknofest Doğal Dil İşleme (NLP) senaryo kategorisinde, Türkcell ve ürünleri (Superonline, Platinum Paket, BİP, Fizy, Lifebox vb.) hakkında kullanıcı yorumlarına dayalı özgün bir entity bazlı duygu analizi gerçekleştirilmiştir. Bu çalışmada, yalnızca yorumların duygusal tonu belirlenmemiş, aynı zamanda yorumların taşıdığı önem veya aciliyet düzeyini belirtmek için "severity" adı verilen ekstra bir kategori de eklenmiştir. "Severity" kolonu, metinde tartışılan konunun aciliyet veya önem derecesini ifade eder; 0 önemsiz, 1 orta derecede önemli ve 2 acil bir durumu belirtir.

Veri işleme süreci, mikro servis mimarisi ile yazılmış bir temizleme servisinden (clean service) geçirilerek başlamıştır. Bu hizmet, verilerin ön işleme aşamasını yönetmiş ve verilerin doğru ve tutarlı bir şekilde analiz edilmesini sağlamıştır. Clean service, FastAPI kullanılarak bir mikro servis olarak yapılandırılmış ve veri temizleme işleminin servis olarak çalışması sağlanmıştır. Bu yapı, verilerin sistemde hızlı ve verimli bir şekilde işlenmesine olanak tanımıştır.

Temizlenmiş veriler, çeşitli Türkcell ürün ve hizmetleri hakkında sosyal medya ve şikayet platformlarından toplanmıştır. Yorumlar, öncelikle entity bazlı duygu analizi modeline tabi tutulmuş, ardından severity derecelerine göre sınıflandırılmıştır. Bu işlem, kullanıcılara sunulan hizmetlerin önem derecesine göre sıralanması ve önceliklendirilmesi açısından büyük bir değer taşımaktadır. Örneğin, acil bir durumu belirten bir yorum (severity: 2) daha fazla dikkat gerektirirken, önemsiz bir yorum (severity: 0) daha az öncelikli kabul edilmektedir.

Bu çalışmada kullanılan model, 'dbmdz/bert-base-turkish-uncased' adlı Türkçe dil modeli üzerine kuruludur. Model, üç sınıflı (0, 1, 2) bir sınıflandırma görevinde kullanılmıştır. Elde edilen sonuçlar, modelin sınıflandırma yeteneklerini göstermektedir. Model, 0 kategorisi için %89.5, 1 kategorisi için %86.9 ve 2 kategorisi için %87.4 doğruluk oranına ulaşmıştır. Bu skorlar, modelin farklı aciliyet derecelerini başarıyla ayırt edebildiğini ve çeşitli Türkcell ürünleri hakkında yapılan yorumların önem derecesini doğru bir şekilde sınıflandırabildiğini göstermektedir.

Çalışmamız, özellikle müşteri geri bildirimlerinin daha etkin bir şekilde yönetilmesi için yeni bir yol sunmaktadır. Severity sınıflandırması sayesinde, kullanıcılar tarafından bildirilen sorunlar veya talepler daha etkili bir şekilde önceliklendirilebilir ve çözüm süreci hızlandırılabilir. Bu, müşteri memnuniyetini artırma ve müşteri deneyimini iyileştirme potansiyeline sahiptir. Gelecekte, bu yaklaşım farklı sektörlerde de uygulanarak, müşteri geri bildirimlerine dayalı hizmet iyileştirme süreçlerine katkı sağlayabilir.




Model indirmek için lütfen iletişime geçin.

https://drive.google.com/drive/folders/1H0nGnQlnkLIxpahd4rLhQ1uWwYWjZ9v7
