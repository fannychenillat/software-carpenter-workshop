import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

def fahr_to_celcius(temp_fahr):
   """Convert farhenheint to celcius"""
   temp_celcius = (temp_fahr - 32) * 5/9
   return temp_celcius

def analyze(data):
    """Perform analysis on mosquitos data
    
    data is a dataframe with columns "temperature", "rainfall", and "Mosquitos"
    
    Perforns a least squares regression, plots  the results and returns the fit parameters """
    
    assert data['temperature'].max()  <70 , "check that temperature is in Celcius"
    
    regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
    parameters = regr_results.params
    rsquared = regr_results.rsquared
    predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
    plt.plot(predicted, data['mosquitos'], 'ro')
    min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
    plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
    plt.show()
    return parameters