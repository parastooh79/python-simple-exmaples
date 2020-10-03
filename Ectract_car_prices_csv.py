# In this exercise, we extract the prices of several cars from an Iranian site 
# And We write them on csv file

import requests
from bs4 import BeautifulSoup
import re 
import csv

d = open("cars.csv","w")

for i in range(5):
    i += 1
    result = requests.get('https://bama.ir/car/all-brands/all-models/all-trims?price=50-60&page=i')
    soup = BeautifulSoup(result.text, 'html.parser')
    val = soup.find_all('h2')
    
    for t in range(27):
        t += 1 
        op = val[t]
        d.write(re.sub(r'\s+',' ',op.text))
        d.write('\n')
        
d.close()
