import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


    
def hiv_data_pipe(amfAR_fp='data/amfAR/countydata.tsv',
              msm_fp="data/CAMP/US_MSM_Estimates_Data_2013.csv",
              employment_fp="data/ACS_14_5YR_employment/ACS_14_5YR_S2301_with_ann.csv",
              income_fp="data/ACS_14_5YR_income/ACS_14_5YR_S1901_with_ann.csv",
              poverty_fp="data/ACS_14_5YR_poverty/ACS_14_5YR_S1701_with_ann.csv"):
    #load Amfar opioid and HIV data, add county code
    opiod_df = pd.read_table(amfAR_fp,header=0)
    opiod_df['county_code'] = opiod_df.STATEFP*1000 + opiod_df.COUNTYFP # build a county code column
    opiod_df['county_code'] = opiod_df.county_code.astype(int)
    #make changes to the amfar dataframe
    #convert from long to wide format
    index_lst = ['county_code', 'COUNTY', 'STATEABBREVIATION', 'YEAR']
    col_lst = ['INDICATOR']
    opiod_df_wide = opiod_df.pivot_table(values='VALUE', index=index_lst, columns=col_lst).reset_index()
    # Focus on just the HIV related data, from 2008 onward
    opiod_df_wide = opiod_df_wide[opiod_df_wide['YEAR'] >= 2008] # subset for years that have hiv data
    cols_to_drop = ['CDC_consult', 'vulnerable_rank']
    #, 'num_SSPs', 'bup_phys', 'drugdep', 'pctunmetneed', 'nonmedpain']
    opiod_df_wide.drop(cols_to_drop, axis=1, inplace=True) # drop unnecessary columns
    
    fill_nan_cols = ['HIVdiagnoses', 'HIVincidence', 'HIVprevalence',
                 'PLHIV', 'drugdeathrate', 'drugdeaths']
    opiod_df_wide[fill_nan_cols] = opiod_df_wide[fill_nan_cols].fillna(0) #fill NaNs for suppressed data with zeroes
    # Subset data to 2015
    opiod_df_15 = opiod_df_wide[opiod_df_wide['YEAR'] == 2015]
    
    pd.options.mode.chained_assignment = None  # default='warn', get rid of annoying warning associated with dropping below
    # drop columns having no 2015 data, will be extraploated from following years later
    opiod_df_15.drop(['num_SSPs', 'bup_phys', 'drugdep', 'pctunmetneed', 'nonmedpain'], axis=1, inplace=True)
    
    # get esimates for num_SSPs, bug_phys, drug_dep, pctunmetneed, and nonmedpain from following years

    #subset opioid related data from one year only
    #number of needle exchange programs (num_SSPs)
    opiod_df_wide_17 = opiod_df_wide[opiod_df_wide['YEAR'] == 2017]
    df_num_SSP = opiod_df_wide_17[['num_SSPs', 'county_code']]

    #number of doctors licensed to rx Buprenorphine (bup_phys)
    df_bup_phys = opiod_df_wide_17[['bup_phys', 'county_code']]

    #percent with drug dependency (drug_dep)
    opiod_df_wide_16 = opiod_df_wide[opiod_df_wide['YEAR'] == 2016]
    df_drugdep = opiod_df_wide_16[['drugdep', 'county_code']]

    #percent unmet drug treatment need (pctunmetneed)
    df_pctunmetneed = opiod_df_wide_16[['pctunmetneed', 'county_code']]

    #percent taken pain meds for nonmedical use (nonmedpain)
    df_nonmedpain = opiod_df_wide_16[['nonmedpain', 'county_code']]
    
    # merge these values back into 2015 dataframe
    #merge opioid related data back to the 2015 dataframe
    opiod_df_15 = opiod_df_15.merge(df_num_SSP, on='county_code')
    opiod_df_15 = opiod_df_15.merge(df_bup_phys, on='county_code')
    opiod_df_15 = opiod_df_15.merge(df_drugdep, on='county_code')
    opiod_df_15 = opiod_df_15.merge(df_pctunmetneed, on='county_code')
    opiod_df_15 = opiod_df_15.merge(df_nonmedpain, on='county_code')
    
    #load Men who have sex with men (MSM) estimate data
    msm_df = pd.read_csv(msm_fp)    #load the data
    msm_df['county_code'] = msm_df.STATEFP*1000 + msm_df.COUNTYFP  # build a county code column
    msm_df['county_code'] = msm_df.county_code.astype(int)
    msm_df['%msm12month'] = 100 * (msm_df.MSM12MTH / msm_df.ADULTMEN) # build a %MSM within last 12 months column
    msm_df['%msm5yr'] = 100 * (msm_df.MSM5YEAR / msm_df.ADULTMEN)     # build a %MSM within last 5years column
    
    cols_to_drop = ['REGCODE', 'DIVCODE', 'STATEFP', 'COUNTYFP', 'CSACODE', 
                'CBSACODE','METDCODE', 'METMICSA', 'CENTOUTL']
    msm_df.drop(cols_to_drop, axis=1, inplace=True) #drop all unneeded columns

    #unemplyment data
    df_employment = pd.read_csv(employment_fp, encoding = "ISO-8859-1", skiprows=1)
    df_employment = df_employment[['Id2', 'Unemployment rate; Estimate; Population 16 years and over']]
    df_employment.columns = ['county_code', 'unemployment_rate']
    
    #poverty data
    df_poverty = pd.read_csv(poverty_fp, encoding="ISO-8859-1", skiprows=1, low_memory=False)
    df_poverty = df_poverty[['Id2', 'Percent below poverty level; Estimate; Population for whom poverty status is determined']]
    df_poverty.columns = ['county_code', 'poverty_rate']
    
    #income data
    df_income = pd.read_csv(income_fp, encoding = "ISO-8859-1", skiprows=1)
    df_income = df_income[['Id2', 'Households; Estimate; Total']]
    df_income.columns = ['county_code', 'household_income']
    
    #merge asfAR hiv/opioid data with CAMP MSM data
    df_main = opiod_df_15.merge(msm_df, on='county_code')

    #merge in ACS data
    df_main = df_main.merge(df_employment, on='county_code')
    df_main = df_main.merge(df_poverty, on='county_code')
    df_main = df_main.merge(df_income, on='county_code')
    
    return df_main

def clean_data(amfAR_fp='data/amfAR/countydata.tsv',
              msm_fp="data/CAMP/US_MSM_Estimates_Data_2013.csv",
              employment_fp="data/ACS_14_5YR_employment/ACS_14_5YR_S2301_with_ann.csv",
              income_fp="data/ACS_14_5YR_income/ACS_14_5YR_S1901_with_ann.csv",
              poverty_fp="data/ACS_14_5YR_poverty/ACS_14_5YR_S1701_with_ann.csv"):
    '''Returns cleaned data'''
    
    cleaned_df = hiv_data_pipe(amfAR_fp=amfAR_fp,
                       msm_fp=msm_fp,
                       employment_fp=employment_fp,
                       income_fp=income_fp,
                       poverty_fp=poverty_fp)
    
    # remove some columns to not be used by model
    cols_to_remove = ['county_code', 'COUNTY', 'STATEABBREVIATION', 'YEAR']
    cleaned_df.drop(columns=cols_to_remove, inplace=True)
    
    # remove cols/rows with nan
    cols_nan = ['mme_percap', 'partD30dayrxrate']
    cleaned_df.drop(columns=cols_nan, inplace=True)
    cleaned_df.dropna(axis='index', inplace=True)
    
    drop_colinear = ['ADULTMEN', 'PLHIV', 'Population', 'Med_AMAT_fac', 'MSM12MTH', 'MSM5YEAR', '%msm5yr', 'TMAT_fac', 'MH_fac', 'Med_MH_fac', 'Med_TMAT_fac', 'SA_fac']
    cleaned_df.drop(columns=drop_colinear, inplace=True)
    return cleaned_df

def get_X_y(df):    
    X = df.copy()
    target_col = 'HIVincidence'
    y = X.pop(target_col)
    return X, y

def remove_outliers(df):
    index_to_remove = df[ df['HIVincidence'] >= 700 ].index
    df.drop(index_to_remove, inplace=True)
    return df 

def create_scatter_plot(x_values, y_values, x_label, y_label, title, filename, display=True):
    '''Either shows or saves a scatterplot'''
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, 6))
    ax.scatter(x_values, y_values)
    ax.set_title(title, fontsize=19)
    ax.set_xlabel(x_label, fontsize=17)
    ax.set_ylabel(y_label, fontsize=17)

    if display:
        plt.show()
    else:
        plt.savefig(f'../images/{filename}.png')  
    plt.close()
       
def draw_corr_heatmap(df):
    font_size = 24
    mpl.rcParams.update({'font.size': font_size})
    mpl.rcParams['xtick.labelsize'] = font_size-5
    mpl.rcParams['ytick.labelsize'] = font_size-5
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(20,20))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", ax=ax);
    

if __name__ == '__main__':
    up_one_dir = '../'
    amfAR_fp = up_one_dir + 'data/amfAR/countydata.tsv'
    msm_fp = up_one_dir + "data/CAMP/US_MSM_Estimates_Data_2013.csv"
    employment_fp = up_one_dir + "data/ACS_14_5YR_employment/ACS_14_5YR_S2301_with_ann.csv"
    income_fp = up_one_dir + "data/ACS_14_5YR_income/ACS_14_5YR_S1901_with_ann.csv"
    poverty_fp = up_one_dir + "data/ACS_14_5YR_poverty/ACS_14_5YR_S1701_with_ann.csv"
    
    
    df = hiv_data_pipe(amfAR_fp=amfAR_fp,
                       msm_fp=msm_fp,
                       employment_fp=employment_fp,
                       income_fp=income_fp,
                       poverty_fp=poverty_fp)
    #max_rows = 10
    #max_columns = None
    #with pd.option_context('display.max_rows', max_rows, 'display.max_columns', max_columns): 
    #    print(df)
    print(df.head())
    
    
    X, y = get_X_y(df)
    
    if False:
        pass
        
    # loop thru and make lots of plots
    if False:
        cols = X.columns
        for col in cols:
            title = col + ' vs ' + y.name
            filename = 'scatter_'+ col + '_vs_' + y.name
            create_scatter_plot(x_values=X[col],
                             y_values=y,
                             x_label=col,
                             y_label=y.name,
                             title=title,
                             filename=filename,
                             display=True)