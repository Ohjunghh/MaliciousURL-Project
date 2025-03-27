## 🚀 ML을 이용한 악성 URL 판별

### 🎯 목표
* 머신러닝 알고리즘을 활용하여 신규 악성 URL 탐지 성능을 향상시키고, 실시간으로 악성 URL을 정확하게 판별하는 시스템을 구축
* 사용자에게 안전한 인터넷 환경을 제공하고, 스미싱, 피싱 등 사이버 범죄 예방에 기여

### 주요 기술 스택

- **프로그래밍 언어** </br> 
  <img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=Python&logoColor=white"/>

- **머신러닝 라이브러리** </br>
  <img src="https://img.shields.io/badge/-scikitlearn-F7931E?style=flat&logo=scikitlearn&logoColor=white"/>

- **웹 프레임워크** </br> 
  <img src="https://img.shields.io/badge/-Django-092E20?style=flat&logo=Django&logoColor=white"/>

### 🔧 구현과정
1. 데이터 수집: Kaggle, Openphish, URLhaus 등에서 악성 URL과 정상 URL 데이터를 수집하여 학습 데이터셋 구축
2. 특징 추출: URL의 길이, WHOIS 정보, TTL 주기 등 다양한 특징을 기반으로 악성 URL을 탐지할 수 있는 특성 분석
3. 머신러닝 모델 학습: Decision Tree, Random Forest, LightGBM 등 다양한 머신러닝 알고리즘을 사용하여 모델 학습 및 최적화
4. 웹 통합: Django 프로젝트에서 URL을 입력받아 모델을 통해 악성 여부를 실시간으로 판별하는 시스템 구축


### 🔍 기능
* URL 판별: 사용자가 입력한 URL을 기반으로 URL 길이, 도메인 정보, TTL 주기 등 다양한 특징을 추출하고, 이를 통해 악성 여부를 실시간으로 판별
