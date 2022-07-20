# Example of chi2 test for independence using smoking and fitness data from
# the stat_cheatsheet.pdf

import numpy as np
import pandas as pd    
import scipy.stats as scs

def make_observed_table(pflag=False):
    """ Makes the fitness level / smoking table in the stat_cheatsheet.pdf """
    columns = ['smoking_habit', 'fit_low','fit_mlow','fit_mhigh','fit_high']
    data = [] 
    data.append(['Never smoked', 113, 113, 110, 159])
    data.append(['Former smokers', 119, 135, 172, 190])
    data.append(['1 to 9 cig. daily', 77, 91, 86, 65])
    data.append(['>= 10 cig. daily', 181, 152, 124, 73])
    df = pd.DataFrame(data = data, columns = columns)
    df.set_index(df['smoking_habit'],inplace = True)
    del df['smoking_habit']
    if pflag:
        print("Observed data")
        print(df)
    return df

def number_table_rows_and_cols(df):
    """ Returns the number of rows and columns in the dataframe """
    return df.shape[0], df.shape[1]

def row_and_col_totals(df, pflag=False):
    """ Returns the row and column totals, row first """
    row_totals = df.sum(axis=1)
    col_totals = df.sum(axis=0)
    if pflag:
        print("\nRow totals:")
        print(row_totals)
        print("\nColumn totals:") 
        print(col_totals)
    return row_totals, col_totals

def make_expected_table(O, row_totals, col_totals, pflag=False):
    """ Makes the expected value table assuming independence """
    GT = O.sum().sum() # grand total
    E = np.zeros((nrow, ncol))
    for i in range(len(row_totals)):
        for j in range(len(col_totals)):
            E[i,j] = row_totals[i]*col_totals[j] / GT
    if pflag:
        print('\nExpected values\n{0}'.format(E.round(2)))
    return E

def calculate_chi2(O, E, pflag=False):
    """ Calculates cell-wise chi2 values, then sums them for total value """
    chi2_table = (O - E)**2 / E # power of numpy
    chi2 = chi2_table.sum().sum()
    if pflag:
        print("\nCell-wise chi2 values:")
        print(chi2_table.round(2))
    return chi2

def display_results(chi2, nrow, ncol, pflag=False):
    """ Displays the results of the 'manual' chi2 analysis """
    ddof = (nrow-1) * (ncol - 1)
    if pflag:
        print("\nThe total chi-square value is {0:0.2f}".format(chi2))
        print("There are {0} degrees of freedom.".format(ddof))
        print("Looking at the chi2 table, the value of p is very, very low.")
        print("p << alpha (~0.05) so will reject null hypothesis that there")
        print("is no relationship between fitness level and smoking habits.\n")


def perform_scipy_analysis(O, pflag):
    """ Performs the same analysis but with scipy stats """
    chi2, p, dof, E = scs.chi2_contingency(O.values)
    if pflag:
        print('*' * 50)
        print("\nScipy stats analysis")
        print("\nScipy's expected table:")
        print(E.round(2))
        print("\nScipy chi-square value is {0:0.2f}".format(chi2))
        print("The probability of this chi-square value assuming the null")
        print("hypothesis is true (fitness and smoking are independent) is")
        print("p = {0:0.2e}.".format(p))
        print("We should reject the null hypothesis.")
        print("A relationship exists between fitness and smoking in this data.")
    return chi2, p

if __name__ == '__main__':
    pflag = True # boolean flag to print results if desired
    O = make_observed_table(pflag)
    nrow, ncol = number_table_rows_and_cols(O) 
    row_totals, col_totals = row_and_col_totals(O, pflag)
    E = make_expected_table(O, row_totals, col_totals, pflag)
    chi2 = calculate_chi2(O, E, pflag)
    display_results(chi2, nrow, ncol, pflag)
    chi2_sp, p_sp = perform_scipy_analysis(O, pflag)    
    
