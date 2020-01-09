# -*- coding: utf-8 -*-
"""
autom plotter
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
    cols={}
    
    #retrieve data
    for row in readCSV:
        if line_num==0:  # get header --> columns name in the csv file       
            header=row          
            
            for i in range(len(header)): # build list for each column
                cols[header[i]] = []
        
        else: # get data and put them into the lists
            for i in range(len(header)): #get the data
                cols[header[i]].append(row[i])
            
        line_num+=1 # iterate
        
# print result        
print(40*'#','\n\n')        
print 
print('My csv file has {} columns\n'.format(len(header)))
       
for i in range(len(header)):       
    print('columns {} is: {}'.format(i,header[i]))

print('\n\n',40*'#')

# plot
plt.figure(figsize=(9,9)) #figure dimention
plt.xlabel('x') # x axis label
plt.ylabel('y') # y axis label
plt.title('\n functions \n') # title

for i in range(1,len(header)):
    plt.plot(
             [float(j) for j in cols[header[0]]], # x
             [float(j) for j in cols[header[i]]], # y
             label='y={}(x)'.format(header[i]), # name for legend
             marker='o', # can be '+' , '^' ,'*','>','o','.'
             markersize=12, # 0 for no marker           
             linestyle='dotted', #'solid', 'dashed', 'dashdot', 'dotted'
             linewidth=2,  #0 for no line            
             ) # name for legend


plt.grid()
plt.legend()

