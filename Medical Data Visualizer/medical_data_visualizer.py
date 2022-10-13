import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
cm_to_m=df['height'] / 100
overwt = pd.DataFrame()
overwt['overweight'] = df['weight'] / cm_to_m ** 2
overwt['overweight'] = overwt['overweight'].astype(int)
overwt.loc[overwt['overweight'] > 25, 'overweight'] = 3323
overwt.loc[overwt['overweight'] <= 25, 'overweight'] = 0
overwt.loc[overwt['overweight'] == 3323, 'overweight'] = 1
df['overweight'] = overwt['overweight']

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df.replace({
    'gluc': {1: 0, 
             2 : 1, 
             3 : 1
            }, 
    'cholesterol': {1: 0, 
                   2 : 1, 
                   3 : 1
                  }
}, inplace=True)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df, id_vars =['cardio'], value_vars =['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    catCount = df_cat.value_counts().reset_index()
    catCount.rename(columns={0: 'total'}, inplace=True)
    sortedCat = catCount.sort_values(by='variable')
    df_cat = sortedCat
    

    # Draw the catplot with 'sns.catplot()'
    catPlot = sns.catplot(x = 'variable', y = 'total', data = df_cat, col = 'cardio', kind='bar', hue = 'value') 
    catPlot.set(xlabel='variable', ylabel='total')

    # Get the figure for the output
    fig = catPlot.fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) 
  & (df['height'] >= df['height'].quantile(0.025)) 
  & (df['height'] <= df['height'].quantile(0.975)) 
  & (df['weight'] >= df['weight'].quantile(0.025)) 
  & (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True




    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,9))

    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap((corr).round(1), center = 0, annot=True, linewidths=.2, mask = mask, vmax = .4, fmt=".1f")
    fig = ax.get_figure()



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
