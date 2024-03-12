# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import warnings
from sklearn.metrics import accuracy_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

warnings.filterwarnings('ignore')

path = 'C:/MaliciousURL-Project/result/real/'
datasets = pd.read_csv(path + 'MLtest.csv',header=0)


# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:35]
y = datasets[['abnormal']]


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


clf = ExtraTreesClassifier(n_estimators=100,
    max_depth=8,
    min_samples_split=3,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42)
clf.fit(X_train, y_train)

pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, pred)
recall = recall_score(y_test, pred)
precision = precision_score(y_test, pred)
f1 = f1_score(y_test, pred)

print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)


#변수중요도
for i, col in enumerate(X_train.columns):   
    print(f'{col} importance : {clf.feature_importances_[i]}') 
print(clf.get_params())