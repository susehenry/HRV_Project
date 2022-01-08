#merge data

import pandas as pd

#a = pd.read_csv("RR.csv")

#b = pd.read_csv("fileb.csv")
#b = b.dropna(axis=1)
#merged = a.merge(b, on='title')
#merged.to_csv("output.csv", index=False)

data = pd.read_csv(r'C:\Users\suseh\OneDrive\Desktop\HRV_Project\Data\user_1\RR.csv', encoding='utf8')
data.head()