import pandas as pd

# Importing the original data files
total_pop_orig = pd.read_csv('SF_total_pop_clean.csv')
median_income_orig = pd.read_csv('SF_median_household_income_clean.csv')
low_income_orig = pd.read_csv('SF_low_income_population_clean.csv')
race_orig = pd.read_csv('SF_race_clean.csv')

# Combining all ACS data into one table
acs_data = total_pop_orig.merge(low_income_orig, on = 'census_tract')
acs_data = acs_data.merge(race_orig, on = 'census_tract')
acs_data = acs_data.merge(median_income_orig, on = 'census_tract')

# Creating all the percentage columns
acs_data['low_income_pop_percent'] = (acs_data['low_income_pop'] / acs_data['total_pop']) * 100
acs_data['hispanic_pop_percent'] = (acs_data['hispanic_pop'] / acs_data['total_pop']) * 100
acs_data['afam_pop_percent'] = (acs_data['afam_pop'] / acs_data['total_pop']) * 100
acs_data['asian_pop_percent'] = (acs_data['asian_pop'] / acs_data['total_pop']) * 100
acs_data['indigenous_pop_percent'] = (acs_data['indigenous_pop'] / acs_data['total_pop']) * 100
acs_data['bipoc_pop_percent'] = (acs_data['bipoc_pop'] / acs_data['total_pop']) * 100

# Dropping rows where [total_pop] is 0
acs_data_clean = acs_data[acs_data['total_pop'] != 0]

# Exporting dataframe as csv file
acs_data_clean.to_csv('SF_acs_data_clean.csv', index = False, header = True)

print('********************** EXPORT COMPLETE **********************')