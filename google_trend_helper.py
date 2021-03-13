# in this practice you should use this libraries
import numpy as np
import pandas as pd
from pytrends.request import TrendReq

def trendhelper():
    pt = TrendReq()

    list_of_words = []

    print('When you have entered all your words, please enter : ! ')

# Get the keywords the user wants

    words = input('Keywords : ')      
    list_of_words.append(words)

    while words != '!':
        words = input('')
        list_of_words.append(words)

# Delete  ' ! ' from the words list 

    del list_of_words[-1]
    
    print('Your words list is ready , Please wait ... ')

# get the history of search as DataFrame

    df = pt.get_historical_interest(keywords=list_of_words)
    # ,year_start=2020,month_start=1 , year_end=2021 , month_end=1
    df.to_csv('d.csv')

# Print the results 

    for i in range(len(list_of_words)):
        s = pd.read_csv('d.csv',header=0,usecols=[list_of_words[i]]).values
        print('Average search for %s  is %f' %(list_of_words[i],s.mean()))

trendhelper()
