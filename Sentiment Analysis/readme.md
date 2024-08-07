## Türkçe BERT ile Duygu Analizi

BERT tabanlı bir model kullanarak Türkçe metinlerde duygu analizi yapmaktadır. Proje kapsamında k-fold çapraz doğrulama yöntemi uygulanmıştır."bert-base-turkish-cased" modeli, Türkçe dilinde büyük ve küçük harf ayrımını dikkate alır. Bu, dil bilgisi ve kelime anlamları açısından önemli olabilir. Cased model kullanmak, özellikle özel isimlerin doğru şekilde anlaşılması ve sınıflandırılması açısından avantaj sağlar.

```
pip install transformers
pip install simpletransformers
```

Kütüphanelerin yüklenilmesi ve içe aktarılması

```
import pandas as pd
from simpletransformers.classification import ClassificationModel
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
import os
import torch
```

Eğitim ve değerlendirme verileri deneme_son.csv dosyasından okunur. K-fold sayısı 10 olarak belirlenmiştir: data klasörü altında erişebilirsiniz.

```
kfold = 10
train_folds_df = pd.read_csv("deneme_son.csv", sep="|", encoding="utf-8")
train_folds_df.head()
```
Veri setine k-fold adında yeni bir sütun eklenir ve her satıra fold numarası atanır:

```
if 'kfold' not in train_folds_df.columns:
    kf = KFold(n_splits=kfold, shuffle=True, random_state=42)
    train_folds_df['kfold'] = -1
    for fold, (train_index, val_index) in enumerate(kf.split(train_folds_df)):
        train_folds_df.loc[val_index, 'kfold'] = fold
```

Her bir fold için model eğitimi ve değerlendirilmesi yapılır. Eğitim verisi olarak belirli bir fold'un dışındaki veriler, validasyon verisi olarak ise fold verileri kullanılır:

```
for fold in range(kfold):
    # Eğitim ve validasyon setlerinin oluşturulması
    train_df = train_folds_df[train_folds_df['kfold'] != fold]
    validation_df = train_folds_df[train_folds_df['kfold'] == fold]

    # SimpleTransformers için veri hazırlanması
    train_df = pd.DataFrame({
        'text': train_df['tweet'],  # Metin kolonu adı değiştirilebilir
        'labels': train_df['labels']
    })
    validation_df = pd.DataFrame({
        'text': validation_df['tweet'],  # Metin kolonu adı değiştirilebilir
        'labels': validation_df['labels']
    })

    # Modelin başlatılması
    model = ClassificationModel('bert',
                                'dbmdz/bert-base-turkish-cased',
                                num_labels=len(le_name_mapping.keys()),
                                use_cuda=True,  # CUDA kullanımı
                                args={'reprocess_input_data': True,
                                      'overwrite_output_dir': True,
                                      'num_train_epochs': 12,
                                      'train_batch_size': 64,
                                      'fp16': False,
                                      'save_model_every_epoch': True,
                                      'save_eval_checkpoints': False,
                                      'output_dir': f'bert_model_fold_merge_{fold}',
                                      'save_steps': 0 })
```

Modelin performansı, her bir fold için değerlendirilir ve genel sonuçlar aşağıdaki gibidir;

| Sınıf        | Precision | Recall | F1-Score | Support |
|--------------|-----------|--------|----------|---------|
| 0  (Nötr)          | 0.846     | 0.824  | 0.861    | 577     |
| 1  (Olumlu)          | 0.86     | 0.872  | 0.885    | 352     |
| 2  (0lumsuz)          | 0.920     | 0.910  | 0.915    | 1305    |
| **Accuracy** | |        |        **0.901**   | **2234**|
| **Macro Avg**| **0.814** | **0.821** | **0.818** | **2234** |
| **Weighted Avg** | **0.855** | **0.854** | **0.854** | **2234** |

Model indirmek için lütfen iletişime geçin.

https://drive.google.com/file/d/1sMf731pnMHduFdz5NnJ_URVxyZJys9SW/view?usp=drive_link

Duygu analizi için oluşturulan Fast api ile servis haline getirdiğimiz kod için api.py dosyasını inceleyebilirsiniz. Servisi çalıştırmak için aşağıdaki kodu kullanabilirsiniz.

```
uvicorn api:app --reload
```


<p align="center">
  <img alt="class_distributions" title="BRAIN-TR" src="https://github.com/tr-brain-com/Acikhack2024TDDI/blob/main/images/Screenshot%20from%202024-08-06%2021-08-16.png">
</p>


