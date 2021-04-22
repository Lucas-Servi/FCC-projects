import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  # Create scatter plot
  #fig, ax = plt.subplots(figsize=(20, 10))
  plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', label='original data',data=df)
  # Create first line of best fit
  years = pd.Series(range(1880,2051))
  res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  plt.plot(years, res.intercept + res.slope*years, 'r', label='fitted line')
    
  # Create second line of best fit
  years2 = pd.Series(range(2000,2051))
  df_2 = df[(df['Year']>= 2000)]
  res_2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
  plt.plot(years2, res_2.intercept + res_2.slope*years2, 'r', label='fitted line 2')
    
  # Add labels and title
  plt.title("Rise in Sea Level")
  plt.legend()
  plt.ylabel("Sea Level (inches)")
  plt.xlabel("Year")
  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
draw_plot()