## Reason Classification

Teknofest 2024'teki Doğal Dil İşleme (NLP) senaryo kategorisi yarışmasında katıldığımız proje, entity bazlı duygu analizi üzerine odaklanmaktadır. Projemizde, Turkcell ve ürünleri hakkında yazılan metinlerde olumsuzluğa sebep olan kategorilerin tespitini amaçlayarak özgünlük sağlamak için veri setine "reason" (sebep) kolonu eklenmiştir. Bu kolon, kullanıcıların olumsuz duygu bildirdiği durumlarda hangi kategoriye (örneğin bayi, fatura, kampanya) dair olumsuzluk yaşadıklarını belirlememize olanak tanımaktadır.

Proje kapsamında kullanılan model, BERT tabanlı "dbmdz/bert-base-turkish-uncased" modelidir. Model, Türkçe metinleri anlamada oldukça başarılıdır ve fine-tuning (ince ayar) işlemiyle özelleştirilmiştir. Modelin çıktılarında olumsuzluğa sebep olan kategoriler şu şekilde ayrılmıştır: 

| Kategori                 | Etiket |
|--------------------------|--------|
| Bayi                     | 0      |
| Diğer                    | 1      |
| Fatura                   | 2      |
| Kampanya                 | 3      |
| Kurumsal                 | 4      |
| KVKK                     | 5      |
| MNP                      | 6      |
| Network                  | 7      |
| Reklam                   | 8      |
| Uygulama                 | 9      |
| Çağrı Merkezi Yetkinlik  | 10     |
| Ürün                     | 11     |

Doğruluk skorları, modelin her bir kategori için ne kadar doğru tahmin yaptığını göstermektedir. Örneğin, "ürün" kategorisinde modelin doğruluk skoru 0.970 (yani %97) olup, oldukça yüksek bir başarıya işaret etmektedir. Öte yandan, "kampanya" kategorisinde doğruluk skoru 0.471, "kurumsal" kategorisinde ise 0.667 olup, bu skorlar daha düşüktür. Bu düşüklükler, veri setinde bu kategorilere ait veri sayısının az olmasından kaynaklanmaktadır. Veri setinin genişletilmesiyle bu kategorilerde de doğruluğun artması beklenmektedir.

| Kategori                 | Doğruluk Skoru |
|--------------------------|----------------|
| Bayi                     | 0.714           |
| Diğer                    | 0.911           |
| Fatura                   | 0.901           |
| Kampanya                 | 0.471           |
| Kurumsal                 | 0.667           |
| MNP                      | 0.508           |
| Network                  | 0.854           |
| Reklam                   | 0.850           |
| Uygulama                 | 0.849           |
| Çağrı Merkezi Yetkinlik  | 0.791           |
| Ürün                     | 0.970           |

Proje, FastAPI ile mikro servis olarak yapılandırılmıştır. Bu yapı, verinin işlenmesi ve analizi için ayrı bir temizleme servisi kullanarak esnek ve modüler bir sistem sunmaktadır. Bu yaklaşım, modelin entegrasyonunu kolaylaştırırken, aynı zamanda performans ve ölçeklenebilirlik açısından avantaj sağlar.

Özetle, projemiz, Türkcell ve ürünleri hakkında yapılan olumsuz geri bildirimlerin nedenlerini anlamaya yönelik özgün bir çözüm sunmaktadır. Bu çözüm, müşteri memnuniyetini artırmaya yönelik stratejik kararların alınmasına yardımcı olabilecek önemli içgörüler sağlayabilir. Model doğruluk skorları, veri setinin genişletilmesiyle birlikte daha da iyileştirilebilir, bu da modelin daha doğru tahminler yapabilmesini sağlayacaktır.

<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-08-02%2021-21-59.png">
</p>

Model indirmek için lütfen iletişime geçin.
https://drive.google.com/file/d/1KpWaAx5UePAZ3Gqgtcvv_mGHf9fqZbvQ/view?usp=drive_link
