# -*- coding:utf-8 -*-
# author:eastchinasea time:2023/5/13.
import pandas as pd
pd.set_option('display.unicode.east_asian_width', True)
df = pd.DataFrame({
    'Chinese': [109, 102, 99],
    'Math': [120, 111, 90],
    'English': [120, 111, 119],
    'Class': 2235
}, index = [0, 1, 2])
print(df)
