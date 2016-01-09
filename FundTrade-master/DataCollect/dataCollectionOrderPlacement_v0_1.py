import os
import time
import re
import pandas as pd
from datetime import datetime

path = "/home/jigish/Downloads/stocksData" #control path

program_start = datetime.now() #recording start time

def Key_Stats(gather="DailyStats"):
    df = pd.DataFrame(columns = ['Day', 'dailyHigh', 'dailyLow', 'Volume', 'adjustedClose', '10pdown'])
#pulling data
#this code looks for all csv files in a particular folder, spare the rest.
    files = []
    for name in os.listdir(path):
        if name.endswith(".csv"):
            #if name.endswith(".csv"):
            if name in ['jnj_10y.csv']: # jnj 10-year
            #if name in ['jnj_all.csv']: # all time
            #if name in ['jnj.csv']: # jnj 1-year
                #print 'name =', name
                files.append(name)
    #print files
    #setting the path to the correct file
    full_file_path = path+'/'+files[0]
    #test full_file_path
    #print "full_file_path =",full_file_path
    #source = pd.read_csv(full_file_path, sep=',', engine='c', nrows = 252) #jnj 1 year
    source = pd.read_csv(full_file_path, sep=',', engine='c', nrows = 2500) #jnj 10 year
    #source = pd.read_csv(full_file_path, sep=',', engine='c', nrows = 11000) #jnj all time
    #pd.unique(df.column_name.ravel())
    #test source
    #get the number of lines read
    #print "number of lines =", numline
    #print out the number of lines read from csv file
    #for x in range (1,250): # jnj 1-year
    for x in range (1,2500): # jnj 10-year
    #for x in range (1,11000): # jnj all time
        day = x
        dailyHigh = float(source['High'][x])
        dailyLow  = float(source['Low'][x])
        adjustedClose = float(source['Close'][x])
        Volume = float(source['Volume'][x])
        ##### 10 percent down marker start
        if x == 1:
            tenPercentDown = 0
        else :
            adjustedClosePrevios = float(source['Close'][x-1])
            # print "adjustedClosePrevios = ",adjustedClosePrevios
            # print "adjustedClose = ",adjustedClose
            # print "iteration = ",x
            PercentDown = 100*((adjustedClose - adjustedClosePrevios) / adjustedClosePrevios)
            # print "percent =", PercentDown
            if PercentDown >= 10:
                tenPercentDown = 1
                print "found winner."
            else :
                tenPercentDown = 0
        ##### 10 percent down marker start
        try:
            df = df.append({'Day':day,
                            'dailyHigh':dailyHigh,
                            'dailyLow':dailyLow,
                            'Volume':Volume,
                            'adjustedClose':adjustedClose,
                            '10pdown':tenPercentDown},
                            ignore_index = True) #'SP500':sp500_value}
        except Exception as e0:
            pass
    # print "jigish change 4"
    # end of for loop
    save = gather.replace(' ','').replace(')','').replace('(','').replace('/','')+('.csv')
    # print(save)
    df.to_csv(save)
Key_Stats()
program_stop = datetime.now()  #recording stop time
# print program run time
print "program run time = ", program_stop - program_start
