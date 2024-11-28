from django.shortcuts import render
from django.http import JsonResponse
import joblib
from feature.feature_extraction import extract_features_from_url 

path=''#pkl path
model = joblib.load(path)

def predict(request):
    if request.method == 'POST':
        # 입력된 URL 가져오기
        url = request.POST.get('url')
        
        # URL에서 특징 추출
        features = extract_features_from_url(url)
        
        # 예측 수행
        probabilities = model.predict_proba([features])
        
        # 예측된 확률을 반환
        response_data = {
            'input_url': url,
            'class_0_probability': probabilities[0][0],
            'class_1_probability': probabilities[0][1]
        }
        
        return JsonResponse(response_data)
    else:
        return render(request, 'predict/predict.html')