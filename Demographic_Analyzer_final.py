import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=(pd.read_csv("fcc-forum-pageviews.csv")).set_index('date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    
    # Setting Up X and Y Variables
    fig, ax = plt.subplots(figsize=(10,5))
    x= df.index
    y= np.array(df['value'])


    ax.plot(x,y) # plots data
    ax.set_xlabel('Date') # X-Label
    ax.set_ylabel('Page Views') # Y-label
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019") #Plot title
    

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():

    # Copy and modify data for monthly bar plot
    df['year'] = pd.DatetimeIndex(df.index).year
    df['month'] = pd.DatetimeIndex(df.index).month

    # Groups together Year and Month. Gets the average value of each pair. Converts into a Multi-Index
    df_bar = df.groupby(['year','month'])['value'].mean()
    df_bar=df_bar.unstack()
    # Draw bar plot
    fig = df_bar.plot.bar(
    xlabel='Years', 
    ylabel='Average Page Views',
    figsize = (15,10), # Figure to Rectangle
    legend= True).figure
    plt.legend(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December' ])

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df['year'] = pd.DatetimeIndex(df.index).year
    df['month'] = pd.DatetimeIndex(df.index).month

    # Draw box plots (using Seaborn)

    fig , axes = plt.subplots(nrows=1,ncols = 2, figsize=(20,10)) # Creates 2 Empty Graph
    # Adding the graph parameters, then axes[0] and axes[1] basically indexes the graph 
    ax_1 = sns.boxplot(x='year', y='value', data=df_box,  ax = axes[0]) 
    ax_2 = sns.boxplot(x='month', y='value', data=df_box , ax=axes[1])

    # Graph Formatting 
    ax_1.set_title('Year-wise Box Plot (Trend)')
    ax_1.set_ylabel('Page Views')
    ax_1.set_xlabel('Year')
    ax_2.set_title('Month-wise Box Plot (Seasonality)')
    ax_2.set_ylabel('Page Views')
    ax_2.set_xlabel('Month')
    ax_2.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig