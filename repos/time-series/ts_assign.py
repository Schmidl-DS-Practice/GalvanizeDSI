import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time_series_helpers import (to_col_vector, 
                                reindex_to_data_frame, 
                                PolynomialBasisExpansion,
                                PolynomialBasisAndDummyizer)


df = pd.read_csv('data/birth.txt')
#print(df)
dates = pd.date_range('1980-01', '2011-01', freq='M')
time = np.arange(1,len(dates)+1)
df['month'] = dates.month
df['year'] = dates.year
#print(time)
df.set_index(dates, inplace=True)
#print(df)
year_avgs = df.groupby(['year'])['num_births'].mean()
month_avgs = df.groupby(['month'])['num_births'].mean()
#print(year_avgs)
#print(month_avgs)

ts = df.num_births
#print(ts.head())

ts.plot(figsize=(16, 4), title="Monthly Births Over Time")
#print(plt.show())
ts['2006':'2010'].plot(figsize=(16, 4), title="Monthly Births Over Time")
#print(plt.show())
seasonal_means = ts.resample('Q-NOV', label='left').mean()
#print(seasonal_means.head())
annual_means = ts.resample('A', label='left').mean()

df['seasonal_means'] = reindex_to_data_frame(seasonal_means, df, 'M')
df['annual_means'] = reindex_to_data_frame(annual_means, df, 'M')

fig, axs = plt.subplots(2, sharey=True, figsize=(14, 6))

df.num_births.plot(ax=axs[0], alpha=0.33)
df.seasonal_means.plot(ax=axs[0])
axs[0].set_title("Seasonal Averages of Births Per Month over Time")

df.num_births.plot(ax=axs[1], alpha=0.33)
df.annual_means.plot(ax=axs[1])
axs[1].set_title("Annual Averages of Births Per Month over Time")

plt.tight_layout()
print(plt.show())