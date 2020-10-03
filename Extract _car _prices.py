#In this exercise, we extract the prices of several cars from an Iranian site

import requests
from bs4 import BeautifulSoup
import re 

for i in range(5):
    i += 1
    result = requests.get('https://bama.ir/car/all-brands/all-models/all-trims?price=50-60&page=i')
    soup = BeautifulSoup(result.text, 'html.parser')
    val = soup.find_all('h2')
    for t in range(27):
        t += 1 
        op = val[t]
        print(re.sub(r'\s+',' ',op.text))
