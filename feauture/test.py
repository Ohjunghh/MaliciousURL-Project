import pandas as pd
import feature_https
import feature_url_shortening
import feature_ttl
import feature_ratio
import feature_count_special_character
import feature_file_extension
import feature_netname
import feature_length

#파이썬 경로 C:\Users\오정현\AppData\Local\Programs\Python\Python310\Scripts
csv_file_path = 'C:/URL/abnormal_dataset/URLhaus+openphish_0111.csv' 
df = pd.read_csv(csv_file_path, header=None, names=['url'])

feature_netname.get_feature_netname(df)#now-create	now-update	end-now	
feature_netname.get_feature_netname(df)#netname
feature_ttl.get_feature_ttl(df)#ttl
feature_length.get_feature_length(df)#len_domain,len_path,len_parameter,len_tld
feature_count_special_character.get_feature_count(df)#count_special
feature_ratio.get_feature_uppercase_ratio(df)
feature_ratio.get_feature_digit_ratio(df)
feature_ratio.get_feature_consonant_vowel(df)
feature_https.get_feature_https(df)#https
feature_file_extension.get_feature_file_extension(df)#file_extension
feature_url_shortening.get_feature_url_shortening(df)#url_shortening


#df.to_csv('C:/URL/after_data processing/test.csv', index=False)