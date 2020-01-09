# -*- coding: utf-8 -*-
"""
more simple but not automatic
"""

import csv
import matplotlib.pyplot as plt

#open csv file an read data
with open('data.csv') as csvfile:
    
    # build reader
    readCSV = csv.reader(csvfile, delimiter=',')
    
    #init line number
    line_num=0
    
    #init header
    header=None
    
    # init data dictionary
    x=[]
    f=[]
    g=[]
    
    #retrieve data
    for row in readCSV:
        if line_num==0:  # get header --> columns name in the csv file       
            header=row 
                   
        else: # get data and put them into the lists
            x.append(float(row[0]))
            f.append(float(row[1]))
            g.append(float(row[2]))
            
        line_num+=1 # iterate
        

# plot
plt.figure(figsize=(9,9)) #figure dimention
plt.xlabel('x') # x axis label
plt.ylabel('y') # y axis label
plt.title('\n Pad functions \n') # title

plt.plot(
         x, # x
         f, # y
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
         x, # x
         g, # y
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

