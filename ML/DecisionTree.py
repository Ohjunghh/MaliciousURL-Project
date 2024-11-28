import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import warnings
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

warnings.filterwarnings('ignore')

project_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_dir, 'ML/urldataset2.csv')
model_output_path = os.path.join(project_dir, 'ML/result/DecisionTree.pkl')

datasets = pd.read_csv(data_path)

# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


clf = DecisionTreeClassifier(
    max_depth=8,
    min_samples_split=3,
    min_samples_leaf=3,
    max_features=None,
    random_state=42)
clf.fit(X_train, y_train)

joblib.dump(clf,model_output_path)

pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, pred)
recall = recall_score(y_test, pred)
precision = precision_score(y_test, pred)
f1 = f1_score(y_test, pred)

print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)

"""
Accuracy: 0.9691666666666666
Recall: 0.9558586139716114
Precision: 0.9818743210017725
F1-Score: 0.9686918260280928
"""