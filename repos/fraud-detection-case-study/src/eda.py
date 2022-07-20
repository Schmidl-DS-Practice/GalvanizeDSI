from datacleanup import Clean
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

data = pd.read_json('../data/data.json')
clean = Clean(data)
X = clean.clean()

def plot_column(data, col, saveloc):
    '''
    Plots counts of Fraud vs Not Fraud for a given column

    Saves plot to images folder
    '''
    plt.figure(figsize=(10,6))
    sns.countplot(x=col, hue='fraud', data=data, palette= 'Set2')
    plt.xlabel(f'{col}',fontsize=18)
    plt.ylabel('Count', fontsize=18)
    plt.title(f'Count of Events per {col}', fontsize=24)
    plt.savefig(saveloc, bbox='tight')

if __name__ == '__main__':
    #Featurization plots
    plot_column(data,'sale_duration','../images/sale_duration')
    plot_column(data,'sale_duration2','../images/sale_duration2')
    plot_column(data,'delivery_method','../images/delivery_method')
    plot_column(data,'has_analytics','../images/has_analytics')
    plot_column(data,'payout_type','../images/payout_type')
    plot_column(data,'fb_published','../images/fb_published')
    plot_column(data,'currency','../images/currency')
    plot_column(data,'channels','../images/channels')
    plot_column(data, 'user_type','../images/user_type')

    #numerical to categorical for viz purposes
    data['num_payouts_greater10'] = np.where(data['num_payouts'] > 10, 1, 0)
    data['user_age_greater30'] = np.where(data['user_age'] > 30, 1, 0)
    plot_column(data,'user_age_greater30','../images/user_age_greater30')
    plot_column(data,'num_payouts_greater10','../images/num_payouts_greater10')