import joblib
import os

# 0. 경로 설정
project_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(project_dir, 'ML', 'result', 'ExtraTree.pkl')

# 1. 저장된 모델 로드
model = joblib.load(model_path)

# 2. 새로운 데이터 불러오기 (예시) 1부터 33까지 
new_data = [
    [100, 10, 4, 5, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
     0, 0, 1]
]  # 새로운 데이터를 적절한 형식으로 입력

# 3. 예측 수행
probabilities = model.predict_proba(new_data)

# 예측된 확률을 출력
for data, probs in zip(new_data, probabilities):
    print("입력 데이터:", data)
    print("클래스 0에 속할 확률:", probs[0])
    print("클래스 1에 속할 확률:", probs[1])
    print()
