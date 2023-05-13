# -*- coding:utf-8 -*-
# author:eastchinasea time:2023/5/13.
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
data = [[109, 120, 120], [93, 96, 92], [83, 83, 82]]
index = [0, 1, 2]
columns = ['语文', '数学', '英语']
df = pd.DataFrame(data = data, index = index, columns = columns)
for i in df.columns:
    series = df[i]
    print(series)
