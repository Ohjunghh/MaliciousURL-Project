import os
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import warnings
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

warnings.filterwarnings('ignore')

project_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(project_dir, 'ML/urldataset2.csv')
model_output_path = os.path.join(project_dir, 'ML/result/KNN.pkl')

datasets = pd.read_csv(data_path)


# 데이터프레임에서 열을 추출하여 새로운 데이터프레임 생성
x = datasets.iloc[:, 1:34]
y = datasets[['abnormal']]

# 훈련 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)



# Bagging 알고리즘 적용
clf  = KNeighborsClassifier(n_neighbors=5,
                            weights='distance', #디폴트는 uniform
                            )
clf.fit(X_train, y_train)

# 예측
pred = clf.predict(X_test)

# 평가
accuracy = accuracy_score(y_test, pred)
recall = recall_score(y_test, pred)
precision = precision_score(y_test, pred)
f1 = f1_score(y_test, pred)

# 결과 출력
print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)


joblib.dump(clf,model_output_path)

"""
Accuracy: 0.8931388888888889
Recall: 0.9049819092680211
Precision: 0.8836830090227199
F1-Score: 0.8942056485988504

"""