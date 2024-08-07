## Bağımlılık Analizi - Dependency Parsing ##

Bu bölüm, problem tanımı uyarınca cümle içerisinde geçen farklı varlıklara yönelik duyguları tespit etmek amacıyla geliştirilmiştir. Yapılan araştırmalar ve gerçekleştirilen çalışmalar incelendiğinde problem çözümüne yönelik olarak <b>Aspect Based</b> ve <b>Entity Based</b> olarak iki farklı yöntem geliştirildiği; bu yöntemlerin  seçimi konusunda da alana özgü verilerin yapısının etkili olduğu fark edilmiştir.<br>

<b>Yönelim Tabanlı (Aspect Based)</b>, bir cümlede veya belgede belirtilen belirli yönlerle ilişkili duyguyu belirleme görevini ifade eder. <br>

<b>Varlık Tabanlı (Entity Based)</b> olarak ifade edilen yapı ise cümle içinde belirlenen varlıklara yönelen duyguların tespitini sağlamayı ifade eder.<br>

Bu çalışma için ürettiğimiz, geliştirdiğimiz veri (ayrıntılı bilgi stats içerisinde mevcuttur), hem entity hem de yönelim tabanlı hibrit bir yapının ortaya konulmasını bizim için gerekli kılmıştır. Bu noktada <b>Bağımlılık Analizi - Dependency Parsing</b> olarak bilinen bir dile ait cümle yapılarının detaylı şekilde incelenmesi ve yorumlanması gerekmiştir. Bağımlılık analizi ile  cümle bölümlendirmesi ve varlık tabanlı ayrıştırma birlikte öğrenilir. Mevcut problemde varlık bazlı veya varlığa yönelik duyguları tespit etmek amacıyla SpaCy kullanarak kural tabanlı bir yapı inşa edilmiştir. Bu kural tabanlı yapı, metinlerin standart cümle yapısına uymayacağı (X verileri vb.) fikrinden hareketle ortaya çıkarılmış, metin içerisinde ki varlıklara yönelen duyguların tespitinde oldukça başarılı sonuçlar elde edilmiştir.<br>

Spacy dilbilimsel olarak hazır bileşenler içeren metin sınıflandırma, etikete dayalı bağımlılıkları analiz etme, cümleleri bölme, morfolojik analiz ve kök ayırma gibi bir çok problemin çözümünde kullanılan bir kütüphanedir. Türkçe'de cümledeki kelimelerin bağımlıklarını bulmak için tr_core_web_trf adında daha önce eğitilmiş, tranformer tabanlı pipeline model kullanıldı. Evrişimli Sinir Ağı tabanlı diğer modellerden tr_core_web_lg, tr_core_web_md gibi modellere göre daha yüksek doğruluk sunduğu için tercih edildi. Model herkese açık bir şekilde erişilebilir ve linkten ulaşılabilir durumdadır.<br>https://github.com/turkish-nlp-suite/turkish-spacy-models

Bağımlılık Analizi (Dependency Parsing) ile hedefimiz bir cümle içerisindeki, sözcükler arasındaki ilişkileri ve ilişki türlerini belirleyerek ilgili cümlenin çözümlemesini sağladığından cümledeki kelime öbeklerini çıkarmada bize yol gösterici olmasıdır. Örneğin "tt çekmiyor vodafone hizmeti rezalet ötesi kesinti oluyor. Turkcell fiyat farkını hak ediyor." cümlesini ele alalım.

<p align="center">
  <img alt="Dependency Parsing Uygulanmış Örnek Bir Cümle" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/dependecy_parsing_01.png" height="300">
</p>

Bağımlılık Analizi uygulanmış ve görsel olarak cümledeki tokenlerin nasıl bir ilişki içinde oldukları aşağıdaki resimde görülmektedir.

![dependency_plot](https://github.com/user-attachments/assets/c9b8cdad-f5c3-4f25-abb8-e3f76b570d9b)

Yukarıdaki tablo için örnek python dilinde yazılmış kod parçacığı ise aşağıdaki gibidir.

```python 
def outDependencyForm(doc, start_idx):
    words_dict = dict()
    row_list = []
    for token in doc:
        ancestors = [t.text for t in token.ancestors]
        children = [t.text for t in token.children]
        row_list.append(
            [(start_idx + token.i), token.text, token.lemma_, token.pos_, token.dep_, token.tag_, ancestors, children])
    df_dependency = pd.DataFrame(row_list, columns=['wordindex', 'token', 'lemma_', 'pos_', 'dep_', 'tag_', 'ancestors',
                                                    'children'])
    df_dependency.reset_index(drop=True, inplace=True)

    return df_dependency
```

Yukarıdaki tabloda iki önemli konu bulunmaktadır. Bunlardan ilki *dep_* kolonu ile verilen her bir kelime veya token'in bağımlılığı bir diğeri ise *pos_* ile belirltilen part-of-speech tagger(metin parçası etiketleme) ile verilen kolondur. Problem çözüm akışımıza göre ilk aşama olarak verilen cümledeki varlıkların çıkartılması için Varlık Etiketi Sınıflandırma modelimiz kullanılmaktadır. Ardından bu modelden çıktı olarak gelen varlıklarla birlikte giriş metninin önce cümlelere sonra da cümleciklere ayırmak için kelimelerin bağlılık ayrıştırmasına göre analiz yapılıp varlık tabanlı cümle ayırma işlemi için aşağıdaki algoritma kullanılmıştır. Algoritma mevcut dil yapısına göre sözcükler ve sözcük grupları analiz edilmiş olup Türkçe diline özgü cümle ayırma işlemi yapmaktadır.

```python
def splitSentencesByDependecies(data):
    sentences = dict()
    sentence = ""
    entities = []
    for index, row in data.iterrows():
        if row["pos_"] != 'PUNCT':
            sentence += row["token"] + " "
        if row["entitiy"] != 'OTHER':
            if len(row["token"]) > 1:
                entities.append([row["token"], row["entityindex"]])
        print(row['token'], row['pos_'], row['dep_'])
        if (((row["pos_"] == 'VERB') and row["dep_"] not in ('nsubj', 'xcomp', 'acl')) or
                (row["pos_"] == 'NOUN' and row["dep_"] in ('advcl', 'ROOT')) or
                (row["pos_"] == 'CCONJ') and ('cc' in row["dep_"])):
            if len(entities) > 0:
                sentences[sentence] = entities
                entities = []
                sentence = ""
    if sentence != "" and len(entities) > 0:
        if 'VERB' not in entities:
            sentences[sentence] = entities
    return sentences
```

Örnek olarak aldığımız "tt çekmiyor vodafone hizmeti rezalet ötesi kesinti oluyor. Turkcell fiyat farkını hak ediyor." cümlesinin ayırma için geliştirilen algoritma çıktı olarak 
*[['tt çekmiyor', ['tt]],  ['vodafone hizmeti rezalet ötesi kesinti oluyor', ['vodafone']] , ['Turkcell fiyat farkını hak ediyor', ['Turkcell']]* şeklinde dizi yapısında bize bu üç farklı veri vermektedir. Üç farklı veride cümleler ve o cümledeki farklı varlıklar bulunmaktadır. Bu çıktıyı sağlayarak amaç bu aşamadan sonraki duygu analizi için cümle ve cümle değerlendirmeleri yapıldıktan sonra değerlendirmenin sahip olacağı varlığı belirlemiş olmaktır.

Geliştirdiğimiz hibrit yaklaşım, oldukça başarılı sonuçlar vermiştir. Gerçek bir örnek üzerinde şu şekilde etkileyici sonuçlar alınmıştır:

<b>Text:</b><br>
tt çekmiyor vodafone hizmeti rezalet ötesi kesinti oluyor. Turkcell fiyat farkını hak ediyor.<br>

<b>Sonuç:</b><br>
![image](https://github.com/user-attachments/assets/c16eb716-dbec-4338-8036-df62a66ad74b)


