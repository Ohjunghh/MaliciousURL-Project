import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler  
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import joblib

# 데이터 불러오기
path = 'C:/MaliciousURL-Project/ML/'
datasets = pd.read_csv(path + 'urldataset2.csv')

# 데이터 전처리
x = datasets.iloc[:, 1:34]
y = datasets['abnormal']

# 학습 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()  
  
X_train = scaler.fit_transform(X_train)  
X_test = scaler.transform(X_test)

# 로지스틱 회귀 모델 생성
clf = LogisticRegression(
    penalty='l2',                    # 규제 유형 ('l1': L1 규제, 'l2': L2 규제)
    C=1.0,                       # 규제 강도의 역수 (값이 작을수록 강한 규제)
    solver='newton-cg',      # 최적화에 사용할 알고리즘
    max_iter=100,               # 최대 반복 횟수
    class_weight=None,            # 클래스 가중치 (None: 균등한 가중치, 'balanced': 불균등한 가중치)
    dual=False,                         # 이중 문제 유형 (True: 이중 문제 사용, False: 원 문제 사용)
    n_jobs=None,                          # 병렬 처리에 사용할 CPU 코어 수 (None: 1개, -1: 모든 코어)
    random_state=42,                        # 난수 발생 시드 값
    tol=0.001                  # 수렴 기준 (작을수록 더 정밀한 계산)
)

# 모델 훈련
clf.fit(X_train, y_train)

# 예측
pred = clf.predict(X_test)

# 성능 평가
accuracy = accuracy_score(y_test, pred)
recall = recall_score(y_test, pred)
precision = precision_score(y_test, pred)
f1 = f1_score(y_test, pred)

# 결과 출력
print("Accuracy:", accuracy)
print("Recall:", recall)
print("Precision:", precision)
print("F1-Score:", f1)

joblib.dump(clf,'C:/MaliciousURL-Project/ML/real_result/Logisitic.pkl')

"""
Accuracy: 0.9414444444444444
Recall: 0.9353186752017812
Precision: 0.9467012226040904
F1-Score: 0.9409755278042226

"""