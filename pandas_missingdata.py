import pandas as pd
import numpy as np
from scipy.stats import mode
import warnings




def impute_values(df_units):

    # Imputing the Missing values
    
    print ("\nMean Units Value\t\t" + str(np.nanmean(df_units['Units'])))
    print ("\nMean Unit Price Value\t\t" + str(np.nanmean(df_units['UnitPrice'])))
    print ("\nMean Percentage Units sold Value\t\t" + str(np.nanmean(df_units['PercentageSold'])))
    print ("\nMaximum Occurence of Store Owner \t\t" + str(mode(df_units["StoreOwner"], nan_policy='omit').mode[0]))

    df_units["Units"].fillna(np.nanmean(df_units['Units']), inplace=True)
    df_units["UnitPrice"].fillna(np.nanmean(df_units['UnitPrice']), inplace=True)
    df_units["PercentageSold"].fillna(np.nanmean(df_units['PercentageSold']), inplace=True)
    df_units["Description"].fillna("Not Available", inplace=True)
    df_units["StoreOwner"].fillna(mode(df_units["StoreOwner"], nan_policy='omit').mode[0], inplace=True)
    df_units["Category"].fillna("Unknown", inplace=True)
    print ("\n\nDataframe with filled missing vales \n\n")
    print df_units[0:25]
    print df_units.isnull().sum()
    


def main():

    df_units = pd.read_csv('D:/dat1/retailMissing.csv')

    print ("Shape of the dataset\t"+str(df_units.shape))
    print df_units[0:20]
    print df_units.dtypes
    # Checks the counts of Null values in dataset
    
    
    print("\nTotal Null/NaN values in dataset\t"+str(df_units.isnull().sum().sum()))
    print("\nFields\t\t   Records Count with NaN Values\n"+str(df_units.isnull().sum()))
    

    # Filtering Columns based on missing values
    '''
    print df_units[df_units['Category'].isnull()]
    print df_units[df_units['Category'].isnull() & df_units['Description'].isnull()]
    '''   
    # Filling missing values with one default value
    '''
    df_filled_zero = df_units.fillna(value=0)
    print df_filled_zero
    print ("\nFilled NaN values Dataframe\n\n"+str(df_filled_zero.isnull().sum()))
    '''

    impute_values(df_units)





if __name__ == '__main__':     # if the function is the main function ...
    warnings.filterwarnings('ignore')
    main() # ...call it