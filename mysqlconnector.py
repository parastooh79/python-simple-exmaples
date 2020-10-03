import requests
import mysql.connector
from bs4 import BeautifulSoup
import re

print('Connecting to database ...')

cnx = mysql.connector.connect(user='parastoo',
                              password='',
                              host='127.0.0.1',
                              database='first')

print('Connected!!')

cursor = cnx.cursor()

for i in range(2):
    i = i + 1
    url = 'https://www.digikala.com/search/category-mobile-phone/?brand[0]=18&brand[1]=1662&brand[2]=10&has_selling_stock=1&sortby=4/page=i'
    headers = {'class':'js-product-url'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    value = soup.find_all('div',attrs={'class':'c-product-box__content'})

    for phone in value:
        name = re.findall(r'(^.*\s)ظرفیت',phone.text)  
        ram = re.findall(r'ظرفیت\s(\d{2,3})',phone.text) 
        price = re.findall(r'\s(.*)تومان',phone.text)
        n = name[0]
        r = ram[0]
        p = price[0].replace('                                    ','')
        sql = 'INSERT INTO digiphones(name , ram , price) VALUES(%s , %s , %s)'
        cursor.execute(sql,(n,r,p,))

cnx.commit()
cursor.close()

print('DONE!')   
