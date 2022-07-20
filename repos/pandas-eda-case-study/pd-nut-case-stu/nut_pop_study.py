import pandas as pd
import matplotlib as plt
import numpy as np
from string import punctuation #to remove punctuation

#what i wrote:
#df = pd.read_csv('nutrition_and_pop_stats.csv')
#df2 = df.groupby('Indicator Name').sum().transpose()
#print('Indicator Name summed up by country\n', df2.iloc[40:-1, 300:301])

#from elsa: 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt  
from string import punctuation #to remove punctuation
def read_df(path):
    '''read in file
    '''
    print('read df')
    return pd.read_csv(path) 
def explore_data(df):
    print(df.head())
    return df
def clean_data(df):
    '''clean up column names
    somewhat janky but got it done faster
    '''
    clean_cols = df.columns.tolist()
    clean_cols = [col.lower().replace(' ', '_').replace('%', 'percent').replace('(', '').replace(')', '').replace("'", '') for col in clean_cols]
    df.columns = clean_cols
    df.columns
    return df
def df_group_by(df):
    '''reset data to make it more manageable
    '''
    df1= df.groupby(['indicator_name', 'country_name']).sum().T #.reset_index()
    df2 = pd.DataFrame(df1)
    print(df2.head())
    return df2
def reset_index(df):
    '''make nested indexes 
    more manageable
    '''
    return df.T.reset_index()
def view_col_data(df):
    '''high level overview
        view all the data collected
    '''
    grouped= df_indexed.groupby('indicator_name')
    for k,v in grouped:
        print(k)
        print("there are these many columns: ", len(grouped))
        return grouped
def df_clean_cols(df):
    '''copy and paste fixed col names
    '''
    df1 = df.T
    resetted = df1.reset_index()
    col_names = resetted.groupby('index').sum()
    return col_names
# def df_of_hiv(df):
#     '''
#     we selected all columns to do with HIV:
#     '''
#     #create new df
#     df_hiv = 
def view_cols(df):
    return df.columns
def df_rename(df):
    '''
    to make selecting specific columns more manageable
    we renamed the columns we had chosen to work with 
    we did not use the view_col_data func to select columns because they are not in alphanumeric order
    in the original df
    '''
    #rename columns
    return  df.rename(columns={'womens_share_of_population_ages_15+_living_with_hiv': 'w_15y+_living_w_hiv', \
                                'adults_ages_15+_newly_infected_with_hiv': '15y+_new_hiv', \
                                'adults_ages_15+_living_with_hiv': '15y+_already_hiv', \
                                'adults_ages_15+_and_children_ages_0-14_newly_infected_with_hiv': 'all_ages_new_hiv', \
                                'adults_ages_15+_and children_0-14_years_living_with_hiv': 'all_ages_already_hiv', \
                                'percent_of_females_ages_15-49_having_comprehensive_correct_knowledge_about_hiv_2_prevent_ways_and_reject_3_misconceptions': 'informed_females_y15-49', \
                                'percent_of_males_ages_15-49_having_comprehensive_correct_knowledge_about_hiv_2_prevent_ways_and_reject_3_misconceptions': 'informed_males_y15-49', \
                                'aids_estimatedDdeaths_unaidsestimates': 'estimated_deaths'}, inplace = True)
if __name__ == "__main__":
    df = read_df('../data/data.csv')
    explore_data(df)
    # breakpoint()
    df_clean = clean_data(df)
    df_clean.head()
    df_grouped = df_group_by(df_clean)
    df_grouped.head()
    df_indexed = reset_index(df_grouped)
    df_indexed.head()
    df_data_snapshot = view_col_data(df)
    #set indicator name as row index
    df_col_index = df_indexed.set_index('indicator_name') #,inplace=True)
    df_col_index.head()
    #tranpose df to clean column headers
    df_T = df_col_index.T
    df_T.head()
    #clean column headers
    df_recleaned = clean_data(df_T)
    df_recleaned
    #view clean column headers
    df_cleaned_view = view_cols(df_recleaned)
    df_cleaned_view   
    #rename selected column headers
    df_renamed = df_rename(df_recleaned) #this does NOT return a df, it just changes the names inplace
    #transpose df back   
    df_T2 = df_recleaned.T
    df_T2
    #put the df through the same groupby cycle to create only 5 rows
    reindex = df_T2.reset_index() 
    reindex
    #create a mask to drop outdated year data
    mask = [x for x in range(1960, 2011)]
    print(mask)
    mask_lst_str = [str(x) for x in mask]
    mask_lst_str
    #drop outdated year data from 1960-2010
    df3 = reindex.drop(mask_lst_str, axis=1)
    df3    
    df3.columns
    #create a multi-index
    df4= df3.set_index(['index', 'country_name'])
    df4
    #select some columns to do with aids and education   
    df_informed_fem = df4.loc['informed_females_y15-49'] #,'informed_males_y15-49']
    df_informed_fem 
    df_informed_male = df4.loc['informed_males_y15-49']
    df_informed_male    
    # f_over_15_living_w_hiv = df4.loc['w_15y+_living_w_hiv']
    # f_over_15_living_w_hiv
    over15_new_hiv = df4.loc['15y+_new_hiv']
    over15_new_hiv
    over15_already_hiv = df4.loc['15y+_already_hiv']
    over15_already_hiv
    # estimated_deaths = df4.loc['estimated_deaths']
    # estimated_deaths
    #create a new df with chosen columns
    df_informed_totals = df_informed_fem + df_informed_male
    df_informed_totals
    #create a new df with chosen columns
    df_already_hiv = pd.merge(left = df_informed_totals, right = over15_already_hiv, how = 'outer', left_index=True, right_index=True, suffixes=('_informed', '_over15_already_hiv')) 
    df_already_hiv #view df
    df_already_hiv.columns #view column titles
    df_already_hiv.pop('unnamed:_60_over15_already_hiv') #remove last column
    df_already_hiv
    #create a new df with chosen columns
    df_new_hiv = pd.merge(left = df_informed_totals, right = over15_new_hiv, how = 'outer', left_index=True, right_index=True, suffixes=('_informed', '_over15_new_hiv')) 
    df_new_hiv.pop('unnamed:_60_over15_new_hiv')
    df_new_hiv
    print("our questions: does being informed lower new cases of HIV?")
    print("is there a difference in being informed and the number of hiv cases?")
    #BY COUNTRY NAME
    #clean column names to use with matplotlib
    reset_new_hiv = df_new_hiv.reset_index()
    reset_new_hiv
    clean_cols = reset_new_hiv.columns.tolist()
    clean_cols = [col.replace('_', '').replace('2011', 'eleven') for col in clean_cols]
    reset_new_hiv.columns = clean_cols
    reset_new_hiv.columns
    reset_new_hiv
    #plot results for new hiv cases
    import matplotlib.pyplot as plt
    y = reset_new_hiv.elevenover15newhiv
    x = reset_new_hiv.countryname 
    plt.scatter(x, y)
    plt.show();
    #clean column names to use with matplotlib
    reset_already_hiv = df_already_hiv.reset_index()
    reset_already_hiv
    clean_cols2 = reset_already_hiv.columns.tolist()
    clean_cols2 = [col.replace('_', '').replace('2011', 'eleven') for col in clean_cols2]
    reset_already_hiv.columns = clean_cols2
    reset_already_hiv.columns
    reset_already_hiv
    #plot results for new hiv cases
    import matplotlib.pyplot as plt
    y = reset_already_hiv.elevenover15alreadyhiv
    x = reset_already_hiv.countryname
    plt.scatter(x, y)
    plt.show();
    #BY INFORMED
    #clean column names to use with matplotlib
    reset_new_hiv = df_new_hiv.reset_index()
    reset_new_hiv
    clean_cols = reset_new_hiv.columns.tolist()
    clean_cols = [col.replace('_', '').replace('2011', 'eleven') for col in clean_cols]
    reset_new_hiv.columns = clean_cols
    reset_new_hiv.columns
    reset_new_hiv
    #plot results for new hiv cases
    import matplotlib.pyplot as plt
    y = reset_new_hiv.elevenover15newhiv
    x = reset_new_hiv.eleveninformed
    plt.scatter(x, y)
    plt.show();
    reset_already_hiv = df_already_hiv.reset_index()
    reset_already_hiv
    clean_cols2 = reset_already_hiv.columns.tolist()
    clean_cols2 = [col.replace('_', '').replace('2011', 'eleven') for col in clean_cols2]
    reset_already_hiv.columns = clean_cols2
    reset_already_hiv.columns
    reset_already_hiv
    #plot results for new hiv cases
    import matplotlib.pyplot as plt
    y = reset_already_hiv.elevenover15alreadyhiv
    x = reset_already_hiv.eleveninformed
    plt.scatter(x, y)
    plt.show();
    print("the y-axis on the plots show that by many, many more numbers, there is a decrease in new cases when people are informed")
data = pd.read_csv('data.csv')