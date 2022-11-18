import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig = plt.subplots(figsize=(16, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    


    # Create first line of best fit
    fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    extYr = pd.DataFrame({"Year" : np.arange(2014,2051)})
    plt.plot(df['Year'].append(extYr["Year"]), fit.intercept + fit.slope*df['Year'].append(extYr["Year"]))

    # Create second line of best fit
    newDf = df.loc[df["Year"] >= 2000]
    fit2 = linregress(newDf['Year'], newDf['CSIRO Adjusted Sea Level'])
    plt.plot(newDf['Year'].append(extYr["Year"]), fit2.intercept + fit2.slope*newDf['Year'].append(extYr["Year"]))

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()