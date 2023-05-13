# -*- coding:utf-8 -*-
# author:eastchinasea time:2023/5/13.
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
df1 = pd.read_excel('12.xlsx', index_col = 0)
print(df1.head())
