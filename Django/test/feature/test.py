import os
import pandas as pd
import feature_day
import feature_https
import feature_url_shortening
import feature_day
import feature_ttl
import feature_ratio
import feature_count_special_character
import feature_file_extension
#import feature_netname
import feature_length

# 현재 스크립트 경로 기준으로 동적 경로 설정
project_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(project_dir, 'result', 't.csv')
output_file_path = os.path.join(project_dir, 'result', 'filextension.csv')

# CSV 파일 읽기
df = pd.read_csv(csv_file_path, header=None, names=['url'])
#df = pd.read_csv(csv_file_path,usecols=['url'])

feature_day.get_feature_day(df)  # now-create, now-update, end-now
#feature_netname.get_feature_netname(df)  # netname
feature_ttl.get_feature_ttl(df)  # ttl
feature_length.get_feature_length(df)  # len_domain, len_path, len_parameter, len_tld
feature_count_special_character.get_feature_count(df)  # count_special
feature_ratio.get_feature_uppercase_ratio(df)
feature_ratio.get_feature_digit_ratio(df)
feature_ratio.get_feature_consonant_vowel(df)
feature_https.get_feature_https(df)  # https
feature_file_extension.get_feature_file_extension(df)  # file_extension
feature_url_shortening.get_feature_url_shortening(df)  # url_shortening

print(df)
df.to_csv(output_file_path, index=False)

#test test