import pandas as pd
import feature_https
import feature_url_shortening
import feature_count_number
import feature_count_special_character
import feature_file_extension
import feature_netname
import feauture_length

#파이썬 경로 C:\Users\오정현\AppData\Local\Programs\Python\Python310\Scripts
csv_file_path = 'C:/URL/abnormal_dataset/URLhaus+openphish_0111.csv' 
df = pd.read_csv(csv_file_path, header=None, names=['url'])


feature_https.get_feature_https(df)
feature_url_shortening.get_feature_url_shortening(df)

#df.to_csv('C:/URL/after_data processing/test.csv', index=False)
