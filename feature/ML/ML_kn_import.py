# -*- coding: utf-8 -*-
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

# 데이터 파일 불러오기
path = 'C:/MaliciousURL-Project/result/real/'
datasets = pd.read_csv(path + 'MLtest.csv',header=0)

X = datasets.iloc[:, 1:35]
y = datasets[['abnormal']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#loaded_model=joblib.load('C:/MaliciousURL-Project/result/real/knn_model_decision_tree.pkl')
loaded_model = joblib.load('C:/MaliciousURL-Project/result/real/knn_model_randomforest.pkl')
#loaded_model = joblib.load('C:/MaliciousURL-Project/result/real/knn_model_extra_tree.pkl')

y_pred =loaded_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)
