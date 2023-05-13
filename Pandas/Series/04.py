import pandas as pd
s1 = pd.Series([120, 110, 116], index = ['Bill', 'Jack', 'Jenny'])
print(s1['Bill'])
print(s1[['Jack', 'Jenny']])
