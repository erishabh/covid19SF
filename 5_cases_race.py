import pandas as pd

# Importing the original data file
covid_race_orig = pd.read_csv('COVID-19__Cases_Summarized_by_Race_and_Ethnicity.csv')

# Dropping the new confirmed case column
covid_race_drop = covid_race_orig.drop(columns = ['New Confirmed Cases'])

# convert date column to datetime
covid_race_drop['Specimen Collection Date'] = pd.to_datetime(covid_race_drop['Specimen Collection Date'])

# Renaming columns
covid_race_ren = covid_race_drop.rename(columns = {'Specimen Collection Date' : 'date', 'Race/Ethnicity' : 'race', 'Cumulative Confirmed Cases' : 'cases'})

# Crearting individual dataframe for each race
covid_asian = covid_race_ren[covid_race_ren['race'] == 'Asian']
covid_indeg = covid_race_ren[covid_race_ren['race'] == 'Native Hawaiian or Other Pacific Islander']
covid_white = covid_race_ren[covid_race_ren['race'] == 'White']
covid_unknown = covid_race_ren[covid_race_ren['race'] == 'Unknown']
covid_hispanic = covid_race_ren[covid_race_ren['race'] == 'Hispanic or Latino/a, all races']
covid_multi = covid_race_ren[covid_race_ren['race'] == 'Multi-racial']
covid_other = covid_race_ren[covid_race_ren['race'] == 'Other']
covid_native = covid_race_ren[covid_race_ren['race'] == 'Native American']
covid_black = covid_race_ren[covid_race_ren['race'] == 'Black or African American']

# Combining all the data frames into one
cases_data = covid_asian.merge(covid_indeg, how = 'outer', on = 'date')
cases_data = cases_data.merge(covid_white, how = 'outer', on = 'date')
cases_data = cases_data.merge(covid_unknown, how = 'outer', on = 'date')
cases_data = cases_data.merge(covid_hispanic, how = 'outer', on = 'date')
cases_data = cases_data.merge(covid_multi, how = 'outer', on = 'date')
cases_data = cases_data.merge(covid_other, how = 'outer', on = 'date')
cases_data = cases_data.merge(covid_native, how = 'outer', on = 'date')
cases_data = cases_data.merge(covid_black, how = 'outer', on = 'date')

# Sort data by datetime
cases_data = cases_data.sort_values(by = ['date']).reset_index(drop = True)

# Exporting dataframe as csv file
cases_data.to_csv('covid_cases_cumulative.csv', index = False, header = True)

print('********************** EXPORT COMPLETE **********************')