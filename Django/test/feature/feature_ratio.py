from urllib.parse import urlparse
import pandas as pd

#대문자 비율
def calculate_uppercase_ratio(url):
    total_chars = len(url)
    uppercase_chars = sum(1 for char in url if char.isupper())

    if total_chars == 0:
        return 0.0

    uppercase_ratio = round(uppercase_chars / total_chars,5)
    return uppercase_ratio

#전체숫자비율
def calculate_digit_ratio(url):
    total_chars = len(url)
    digit_chars = sum(1 for char in url if char.isdigit())

    if total_chars == 0:
        return 0.0

    digit_ratio = round(digit_chars / total_chars,5)
    return digit_ratio

#호스트 자음/모음+자음 비율
def calculate_consonant_vowel_ratio(url):
    parsed_url = urlparse(url)
    host = parsed_url.netloc

    vowels = set("aeiouAEIOU")
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")

    vowel_count = sum(1 for char in host if char in vowels)
    consonant_count = sum(1 for char in host if char in consonants)

    total_chars = vowel_count + consonant_count

    if total_chars == 0:
        return 0.0

    consonant_vowel_ratio =round(consonant_count / total_chars,5)
    return consonant_vowel_ratio

def get_feature_uppercase_ratio(dataframe):
    #dataframe['url'] = dataframe['url'].fillna('').astype(str)
    dataframe['uppercase'] = dataframe['url'].apply(calculate_uppercase_ratio)

def get_feature_digit_ratio(dataframe):
    #dataframe['url'] = dataframe['url'].fillna('').astype(str)
    dataframe['digit_ratio'] = dataframe['url'].apply(calculate_digit_ratio)

def get_feature_consonant_vowel(dataframe):
    #dataframe['url'] = dataframe['url'].fillna('').astype(str)
    dataframe['consonant_vowel'] = dataframe['url'].apply(calculate_consonant_vowel_ratio)