import pandas as pd

def get_feature_count(dataframe):
    # 각 URL에 대해 결과 계산 및 DataFrame에 열 추가
    for i, url in enumerate(dataframe['url']):
        result = count_special_characters(url)
        for char, count in result.items():
            dataframe.at[i, f'\'{char}\''] = count

def count_special_characters(url):
    special_characters = {'%': 0, '$': 0, '=': 0, '@': 0, '?': 0, 
                        '&': 0, '#': 0, '.': 0, '_': 0,
                        '-': 0, ';': 0, '{': 0, '}': 0,
                        '[': 0, ']': 0, '|': 0, '+': 0, '*': 0}
    for char in url:
        if char in special_characters:
            special_characters[char] += 1
    return special_characters
