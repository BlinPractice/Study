# Day_04_02_pandas.py

import pandas as pd

df = pd.read_csv('./data/dummy.csv')
print(df)
print(type(df), '\n')

print(df['population'])
print(df.population)
print()
print(df.population.index)
print(df.population.values)
print(type(df.population.values))
print('-' * 30)

# Quiz : df로부터 가운데 위치한 year 컬럼의 값만 출력하세요. (2가지)
print(f"pandas : {df.year.values}")
print(f"numpy  : {df.values[:, 1]}")
