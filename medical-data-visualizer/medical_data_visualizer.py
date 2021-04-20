import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = np.where(df['weight']/(df['height']/100).pow(2)> 25, 1,0)
# BMI by dividing their weight in kilograms by the square of their height in meters. If that value
# is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
df['cholesterol'] = np.where(df['cholesterol'] >1,1,0)
df['gluc'] = np.where(df['gluc'] >1,1,0)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1,
# make the value 0. If the value is more than 1, make the value 1.
# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc',
  # 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = pd.melt(df, value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
  df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
  df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().to_frame('total').reset_index()
   
  # Draw the catplot with 'sns.catplot()'
  g = sns.catplot(x = 'variable',y = 'total', hue = 'value',col = 'cardio', data = df_cat,kind = 'bar')

  fig = g.fig
  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = df[
    (df['ap_lo'] <= df['ap_hi'])
    & (df['height'] >= df['height'].quantile(0.025))
    & (df['height'] <= df['height'].quantile(0.975))
    & (df['weight'] >= df['weight'].quantile(0.025))
    & (df['weight'] <= df['weight'].quantile(0.975))
    ]

  # Calculate the correlation matrix
  corr = round(df_heat.corr(),1)
  #display(corr)
  # Generate a mask for the upper triangle
  mask = np.zeros_like(corr)
  mask[np.triu_indices_from(mask)] = True


  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(20, 10))

  # Draw the heatmap with 'sns.heatmap()'
  ax = sns.heatmap(corr, mask=mask, vmax=.3, square=True,annot=True,fmt='.1f')

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
