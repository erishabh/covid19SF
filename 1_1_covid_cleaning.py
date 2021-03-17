import pandas as pd

# Importing the original data file
covid_orig = pd.read_csv('COVID-19_Cases_and_Deaths_Summarized_by_Geography.csv')

# Deleting unecesary columns - [area_type, last_updated_at, deaths, rate]
covid_drop = covid_orig.drop(columns = ['area_type', 'last_updated_at', 'deaths', 'rate'])

# Converting data in [id] to string
covid_drop['id'] = covid_drop['id'].astype(str)

# Extracting cencus tract number from [id] column
covid_drop['census_tract_unf'] = covid_drop['id'].str.extract(r'(.{6}$)')
covid_drop['census_tract_first'] = covid_drop['census_tract_unf'].str.extract(r'(^.{4})')
covid_drop['census_tract_last'] = covid_drop['census_tract_unf'].str.extract(r'(.{2}$)')
covid_drop['census_tract_last'] = covid_drop['census_tract_last'].replace({'00' : ''})
covid_drop['census_tract'] = covid_drop['census_tract_first'].str.cat(covid_drop['census_tract_last'], sep = '.')
covid_drop['census_tract'] = covid_drop['census_tract'].replace(regex = r'(\.)$', value = '')
covid_drop['census_tract'] = covid_drop['census_tract'].replace(regex = r'(^0)', value = '')

# Dropping all columns used in census tract extraction
covid_clean = covid_drop.drop(columns = ['census_tract_unf', 'census_tract_first', 'census_tract_last', 'id'])

# Cleaning [acs_population] column
covid_clean['acs_population'] = covid_clean['acs_population'].replace(regex = r'(,)', value = '')

# Creating [covid_percent] column
covid_clean['acs_population'] = covid_clean['acs_population'].astype(int)
covid_clean['covid_percent'] = covid_clean['count'] / covid_clean['acs_population']

# Reorder columns in dataframe
covid_clean = covid_clean[['census_tract', 'count', 'acs_population', 'covid_percent', 'multipolygon']]

# Sorting the dataframe based on census tract
covid_clean = covid_clean.sort_values(by = ['census_tract'], ascending = True)

# Exporting dataframe as csv file
covid_clean.to_csv('SF_covid_concentration_clean.csv', index = False, header = True)

print('********************** EXPORT COMPLETE **********************')