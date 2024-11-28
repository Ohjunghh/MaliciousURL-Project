import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import warnings
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

warnings.filterwarnings('ignore')


project_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_dir, 'ML/urldataset2.csv')
model_output_path = os.path.join(project_dir, 'ML/result/ExtraTree.pkl')

datasets = pd.read_csv(data_path)

# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)


clf = ExtraTreesClassifier(max_depth= 10,          
 max_features= 'sqrt',
 min_samples_leaf=1,      
 min_samples_split= 5,   
 n_estimators= 250,
 random_state= 42
)
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
Accuracy: 0.92975
Recall: 0.9116059003618147
Precision: 0.9456634715325095
F1-Score: 0.9283224215627923
"""