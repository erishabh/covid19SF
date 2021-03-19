import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Control if the plots are displayed or not
show_plots = False

# Importing the original data file
covid_data = pd.read_csv('SF_acs_covid_combined_data_clean.csv')

# Create plots if show_plots == True
if (show_plots):
    # Creating the scatterplots [covid_percent vs low_income_pop_percent]
    low_income_plot = sns.regplot(data = covid_data, x = 'low_income_pop_percent', y = 'covid_percent')
    low_income_plot.set_xlabel('% of Tract Population with Low Income')
    low_income_plot.set_ylabel('% of Tract Population with Covid-19 Diagnosis')
    low_income_plot.set_title('Low Income Population vs Covid-19 Diagnosis by Percent of Tract Populaton')
    plt.show()

    # Creating the scatterplots [covid_percent vs median_household_income]
    median_plot = sns.regplot(data = covid_data, x = 'median_household_income', y = 'covid_percent')
    median_plot.set_xlabel('Median Household Income ($)')
    median_plot.set_ylabel('% of Tract Population with Covid-19 Diagnosis')
    median_plot.set_title('Median Household Income vs Covid-19 Diagnosis by Percent of Tract Populaton')
    plt.show()

    # Creating the scatterplots [covid_percent vs bipoc_pop_percent]
    bipoc_plot = sns.regplot(data = covid_data, x = 'bipoc_pop_percent', y = 'covid_percent')
    bipoc_plot.set_xlabel('% of Tract Population who are BIPOC')
    bipoc_plot.set_ylabel('% of Tract Population with Covid-19 Diagnosis')
    bipoc_plot.set_title('BIPOC Population vs Covid-19 Diagnosis by Percent of Tract Populaton')
    plt.show()

    # Creating the scatterplots [covid_percent vs hispanic_pop_percent]
    hispanic_plot = sns.regplot(data = covid_data, x = 'hispanic_pop_percent', y = 'covid_percent')
    hispanic_plot.set_xlabel('% of Tract Population who are Hispanic or Latino')
    hispanic_plot.set_ylabel('% of Tract Population with Covid-19 Diagnosis')
    hispanic_plot.set_title('Hispanic or Latino Population vs Covid-19 Diagnosis by Percent of Tract Populaton')
    plt.show()

    # Creating the scatterplots [covid_percent vs afam_pop_percent]
    afam_plot = sns.regplot(data = covid_data, x = 'afam_pop_percent', y = 'covid_percent')
    afam_plot.set_xlabel('% of Tract Population who are African American or Black')
    afam_plot.set_ylabel('% of Tract Population with Covid-19 Diagnosis')
    afam_plot.set_title('African American or Black Population vs Covid-19 Diagnosis by Percent of Tract Populaton')
    plt.show()

    # Creating the scatterplots [covid_percent vs asian_pop_percent]
    asian_plot = sns.regplot(data = covid_data, x = 'asian_pop_percent', y = 'covid_percent')
    asian_plot.set_xlabel('% of Tract Population who are Asian')
    asian_plot.set_ylabel('% of Tract Population with Covid-19 Diagnosis')
    asian_plot.set_title('Asian Population vs Covid-19 Diagnosis by Percent of Tract Populaton')
    plt.show()

    # Creating the scatterplots [covid_percent vs indigenous_pop_percent]
    indeg_plot = sns.regplot(data = covid_data, x = 'indigenous_pop_percent', y = 'covid_percent')
    indeg_plot.set_xlabel('% of Tract Population who are Indigenous')
    indeg_plot.set_ylabel('% of Tract Population with Covid-19 Diagnosis')
    indeg_plot.set_title('Indigenous Population vs Covid-19 Diagnosis by Percent of Tract Populaton')
    plt.show()
    
    print('********************** ALL PLOTS SHOWN **********************')
else:
    print('********************** NOT SHOWING PLOTS **********************')