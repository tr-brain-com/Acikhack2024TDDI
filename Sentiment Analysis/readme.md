## Türkçe BERT ile Duygu Analizi

BERT tabanlı bir model kullanarak Türkçe metinlerde duygu analizi yapmaktadır. Proje kapsamında k-fold çapraz doğrulama yöntemi uygulanmıştır.

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
