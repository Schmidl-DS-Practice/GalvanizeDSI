import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.use('ggplot')

df = pd.read_csv('data/nyt1.csv')
print(df.info())
#print(df.describe())
df['CTR'] = df['Impressions'] + df['Clicks']
#print(df)
data = df.hist(figsize=(12, 5), grid=False)
plt.tight_layout() 
#plt.show()
df1 = df['Signed_In'].dropna().sum()
print(df1)
