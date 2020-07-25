import requests
import csv
from bs4 import BeautifulSoup

filename = 'signals.csv'

f = csv.writer(open(filename, 'w', newline=''))
f.writerow(['Name', 'Price', 'Growth', 'Monthly Growth', 'Subs', 'Funds', 'Weeks', 'Trades', 'Winrate', 'DD'])

html = requests.get('https://www.mql5.com/en/signals/mt4/list/')
soup = BeautifulSoup(html.text, 'html.parser')

amountOfPages = int(soup.find(class_="paginatorEx").findAll('a')[-1].text)
