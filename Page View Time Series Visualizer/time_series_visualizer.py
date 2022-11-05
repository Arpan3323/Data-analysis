import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data 
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates= ['date'], index_col='date')

# Clean data
df = df.loc[(df['value'] > df['value'].quantile(0.025)) & (df['value'] < df['value'].quantile(0.975)) ]


def draw_line_plot():
    # line plot
    fig, axes = plt.subplots(figsize=(16, 6))
    axes.plot(df.index, df['value'], color = 'red')
    axes.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    axes.set_xlabel('Date')
    axes.set_ylabel('Page Views')







    # Save image and return fig
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df
    ddf = df_bar.reset_index()
    ddf['month'] = pd.DatetimeIndex(ddf['date']).month
    ddf['year'] = pd.DatetimeIndex(ddf['date']).year
    ddf.replace({
        'month': {1: 'January', 
                 2 : 'February', 
                 3 : 'March',
                 4 : 'April',
                  5 : 'May',
                  6 : 'June',
                  7 : 'July',
                  8 : 'August',
                  9 : 'September',
                  10 : 'October',
                  11 : 'November',
                  12 : 'December',
                }}, inplace=True)
    pd.to_datetime(ddf['year'])
    
    ddf.drop(['date'], axis=1,inplace=True)
    #Sorting the months by categorizing
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    ddf["month"] = pd.Categorical(ddf["month"], categories=months)
    
    df_pivot = pd.pivot_table(
     ddf,
     values="value",
     index="year",
     columns="month",
     aggfunc=np.mean
    )
    axes = df_pivot.plot(kind="bar")
    axes.legend(title='Months')
    axes.set_xlabel('Years')
    axes.set_ylabel('Average Page Views')
    fig=axes.get_figure()
    fig.set_size_inches(16,6)





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    df_box["month"] = pd.Categorical(df_box["month"], categories=months)
    # box plots (Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))
    sns.boxplot(ax=axes[0], x='year', y='value', data=df_box)
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    sns.boxplot(ax=axes[1], x='month', y='value', data=df_box)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    





    # Save image and return fig
    fig.savefig('box_plot.png')
    return fig
