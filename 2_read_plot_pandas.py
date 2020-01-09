# -*- coding: utf-8 -*-
"""
simplest and most power full but requieres pandas
 - pip install pandas
 ou
 - conda install pandas
     https://pandas.pydata.org/pandas-docs/stable/install.html
"""

import pandas as pd
import matplotlib.pyplot as plt

#import csv file in a pandas dataframe
df=pd.read_csv('data.csv',sep=',')


#fast plot
df.set_index('x').plot()

#slow plot
plt.figure(figsize=(9,9)) #figure dimention
plt.xlabel('x') # x axis label
plt.ylabel('y') # y axis label
plt.title('\n Pad functions \n') # title

plt.plot(
          df['x'], # x
          df['f'], # y
          label='y=f(x)', # name for legend
          marker='o', # can be '+' , '^' ,'*','>','o','.'
          markersize=8, # 0 for no marker
          markeredgecolor='blue', 
          markerfacecolor='lightblue',
          linestyle='dotted', #'solid', 'dashed', 'dashdot', 'dotted'
          linewidth=5,  #0 for no line
          color='magenta' # if commented automatic color management                
          ) # name for legend

plt.plot(
          df['x'], # x
          df['g'], # y
          label='y=g(x)', # name for legend
          marker='^', # can be '+' , '^' ,'*','>','o','.'
          markersize=6, # 0 for no marker
          markeredgecolor='green',
          markerfacecolor='olive',
          linestyle='dashdot', #'solid', 'dashed', 'dashdot', 'dotted'
          linewidth=2,  #0 for no line
          color='red'  # if commented automatic color management          
          ) # name for legend


plt.grid() # display grid
plt.legend() # display legend

