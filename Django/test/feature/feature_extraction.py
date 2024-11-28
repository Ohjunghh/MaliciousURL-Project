import pandas as pd
import feature.feature_day
import feature.feature_https
import feature.feature_url_shortening
import feature.feature_ratio
import feature.feature_count_special_character
import feature.feature_file_extension
import feature.feature_length
import feature.feature_ttl

def extract_features_from_url(url):
    df = pd.DataFrame([url], columns=['url'])

    # 특징 추출 함수 호출
    feature.feature_day.get_feature_day(df)
    feature.feature_ttl.get_feature_ttl(df)
    feature.feature_length.get_feature_length(df)
    feature.feature_count_special_character.get_feature_count(df)
    feature.feature_ratio.get_feature_uppercase_ratio(df)
    feature.feature_ratio.get_feature_digit_ratio(df)
    feature.feature_ratio.get_feature_consonant_vowel(df)
    feature.feature_https.get_feature_https(df)
    feature.feature_file_extension.get_feature_file_extension(df)
    feature.feature_url_shortening.get_feature_url_shortening(df)

    # URL 열 제거
    df = df.drop(columns=['url'])

    # NaN 값 처리: NaN 값을 특정 기본값으로 대체
    default_values = [7023.379156,293.3813667,555.6380389,7582.230908,  #'feature_day'
                    5655.256278,  #'feature_ttl':
                    16.27976667,26.96641111,9.210833333,3.050838889, #'feature_length': [
                    0.329705556, 0.000333333,0.486538889,0.002522222,0.196255556,0.29955,0.003222222,2.028816667,0.3936,1.335477778,0.019455556,0.000683333,0.000677778,0.002883333,0.002883333,0.000277778,0.050633333,0.000595234,  #'feature_count_special_character': [
                    #'feature_ratio_uppercase': 
                    0.026169871,
                    #'feature_ratio_digit': 
                    0.059951231,
                    #'feature_ratio_consonant_vowel': 
                    0.645634261,
                    #'feature_https':
                    0.545633333,
                    #'feature_file_extension': 
                    0.406233333,
                    #'feature_url_shortening': 	
                    0.006977778
                    ]

    # NaN 값을 리스트에 있는 기본값으로 대체
    df = df.fillna(pd.Series(default_values, index=df.columns))

    # 필요한 특징만 추출하여 리스트 형태로 반환
    features = df.iloc[0].astype(float).tolist()
    return features
