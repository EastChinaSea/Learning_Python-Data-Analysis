# -*- coding:utf-8 -*-
# author:eastchinasea time:2023/5/13.
import pandas as pd
s1 = pd.Series([120, 110, 116], index = ['Bill', 'Jack', 'Jenny'])
print(s1['Bill': 'Jenny'])
