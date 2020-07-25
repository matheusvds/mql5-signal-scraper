import csv
import requests
from bs4 import BeautifulSoup

filename = 'signals.csv'

f = csv.writer(open(filename, 'w', newline=''))
f.writerow(['Name', 'Price', 'Growth', 'Monthly Growth', 'Subs', 'Funds', 'Weeks', 'Trades', 'Winrate', 'DD'])

html = requests.get('https://www.mql5.com/en/signals/mt5/list/')
soup = BeautifulSoup(html.text, 'html.parser')

amountOfPages = int(soup.find(class_="paginatorEx").findAll('a')[-1].text)

for pageNumber in range(1, amountOfPages):
    print('## Page: ' + str(pageNumber))
    requestedHtml = requests.get('https://www.mql5.com/en/signals/mt4/list/page' + str(pageNumber))
    pageSoup = BeautifulSoup(requestedHtml.text, 'html.parser')

    page = pageSoup.find(class_="signals-table")
    list = page.findAll(class_="row signal")

    for row in list:
        name = row.find('span', { 'class' : 'name' }).text
        price = row.find('div', { 'class' : 'col-price' }).text
        growth = row.find('div', { 'class' : 'col-growth' }).text
        monthGrowth = row.find('div', { 'class' : 'col-growth' }).get('title', 'no title')
        subs = row.find('div', { 'class' : 'col-subscribers' }).text
        funds = row.find('div', { 'class' : 'col-facilities' }).text
        weeks = row.find('div', { 'class' : 'col-weeks' }).text
        trades = row.find('div', { 'class' : 'col-trades' }).text
        winrate = row.find('div', { 'class' : 'col-plus' }).text
        dd = row.find('div', { 'class' : 'col-drawdown' }).text
        
        print(name)
        f.writerow([name, price, growth, monthGrowth, subs, funds, weeks, trades, winrate, dd])