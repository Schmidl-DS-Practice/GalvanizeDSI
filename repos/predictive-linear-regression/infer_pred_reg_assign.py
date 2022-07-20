import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
import numpy as np
import statsmodels.api as sms


df = pd.read_csv('data/balance.csv')
#_ = scatter_matrix(df, figsize=(20,20), alpha=0.5, s=100)
#print(plt.show())

df['Gender'] = np.where(df['Gender'] == 'Female', 1, 0)
df['Student'] = np.where(df['Student'] == 'Yes', 1, 0)
df['Married'] = np.where(df['Married'] == 'Yes', 1, 0)

df = pd.get_dummies(df)
df.drop('Ethnicity_African American', axis=1, inplace=True)

x = df.drop('Balance', axis=1)
x.drop('Unnamed: 0', axis=1, inplace=True)
x.drop('Age', axis=1, inplace=True)
y = df['Balance']

model = sms.OLS(y, x).fit()
sm = model.summary()
y_hat = model.predict(x)
#print(sm)

ss_res = np.power(y_hat-y, 2)
#print(ss_res)

#fig, ax = plt.subplots()

#ax.scatter(y_hat, ss_res)
#ax.hist(y, bins=100)

df.plot(kind='scatter', y='Balance', x='Ethnicity_Caucasian', edgecolor='none', figsize=(12, 5))

print(plt.show())

# b = np.linalg.inv(x.T.dot(x)).dot(x.T).dot(y)
# #print(b)
# y_hat = np.mean(y)
# ss_tot = np.sum(np.power(y-y_hat, 2))
# #print(ss_tot)
# #print(ss_res)
# r2 = 1 - ss_res/ss_tot
# #print(r2)