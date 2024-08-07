## Twitter ile Aşağılayıcı Dil Tespiti Uygulaması

Bu uygulama, Teknofest Aşağılayıcı Dil Tespiti yarışması kapsamında geliştirilen yapay zeka modelinin uygulamasını göstermek amacıyla geliştirilmiştir. Uygulama Python ile Streamlit kütüphanesi kullanılarak geliştirilmiştir. Uygulama ve bölümlerine ilişkin açıklamalar şu şekildedir:,

**1. Bölüm, Uygulama Ana Sayfası**

![Screenshot from 2023-03-21 14-20-46](https://user-images.githubusercontent.com/118043046/228529869-4667ed1f-ad47-473c-9348-1cacde70a845.png)

**2. Bölüm, Söylem Kategori Tespiti**

Bu bölümde kullanıcıdan bir metin istenilmektedir. Bu metin daha sonra yarışma kapsamında geliştirilen model ile değerlendirilerek alınan sonuçlar kullanıcıya gösterilmektedir. Daha sonra geri bildirim için kullanıcının bu kategori doğrulaması veya yanlış tahmin durumunda metnin gerçek kategorisi için geri bildirim göndermesi beklenilmektedir.

![Screenshot from 2023-03-21 14-22-01](https://user-images.githubusercontent.com/118043046/228530104-3f396290-1e5b-4ac7-9d4c-1ee3fa28c49d.png)

**3. Bölüm, Aşağılayıcı Söylemlerin Twitter İle Canlı Olarak Tespit Edlmesi**

Bu bölümde, #braintr hastag'ına gelen mesajlar otomatik olarak model tarafından değerlendirilmekte, ayrıca dağılım dairesel grafik ile tan tarafta gösterilmektedir. Sistem canlı olarak çalışmaktadır. Sürekli kendisini yenileyen sistem gelen twitleri kısa bir gecikme ile yakalamakta (30 saniye) ve model ile değerlendirmektedir. Grafik de anlık olarak bu işlemler sonucunda güncellenmektedir.

![Screenshot from 2023-03-21 14-23-09](https://user-images.githubusercontent.com/118043046/228531431-183e3b12-f00c-4352-84d7-747417f86aad.png)


**4. Bölüm, Geri Bildirim**

Bu bölüm ise kullancılardan gelen gei bildirimlerin kaydını ve bu kayıtların kategorisel olarak dağılımını grafiksel olarak göstermektedir. Burada toplanan veriler daha sonra modelin eğitiminde kullanılacak şekilde senaryo edilmiştir.

![Screenshot from 2023-03-21 14-23-46](https://user-images.githubusercontent.com/118043046/228531855-50699c11-81f7-4d32-8c57-72300561c71c.png)
