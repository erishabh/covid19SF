import pandas as pd

# Importing the original data file
cases_orig = pd.read_excel('covid_cases_cumulative.xlsx')

# Creating a copy of the table for cleaning
cases_clean = cases_orig.copy()

# Combining some columns
cases_clean['Other'] = cases_clean['unknown'] + cases_clean['multi'] + cases_clean['other_other']
cases_clean['Indigenous'] = cases_clean['native'] + cases_clean['native_am']

# Dropping some columns
cases_clean = cases_clean.drop(columns = ['native', 'unknown', 'multi', 'other_other', 'native_am'])

# Exporting dataframe as csv file
cases_clean.to_csv('covid_cases_cumulative_clean.csv', index = False, header = True)

print('********************** EXPORT COMPLETE **********************')
