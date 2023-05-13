# -*- coding:utf-8 -*-
# author:eastchinasea time:2023/5/12.
import pandas as pd
# 解决数据输出时列明不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_excel('1.xlsx')
print(df.head())
