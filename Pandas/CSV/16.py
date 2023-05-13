# -*- coding:utf-8 -*-
# author:eastchinasea time:2023/5/13.
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_csv('16.csv', encoding = 'utf-8')
print(df1.head())
