import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

import warnings
warnings.filterwarnings('ignore')

path = 'C:/MaliciousURL-Project/ML/'
datasets = pd.read_csv(path + 'urldataset.csv')


# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]

#print(x.info())

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

clf = joblib.load('C:/MaliciousURL-Project/RandomForest.pkl')


y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)

