import requests
import csv
from bs4 import BeautifulSoup

filename = 'signals.csv'

f = csv.writer(open(filename, 'w', newline=''))
f.writerow(['Name', 'Price', 'Growth', 'Monthly Growth', 'Subs', 'Funds', 'Weeks', 'Trades', 'Winrate', 'DD'])

html = requests.get('https://www.mql5.com/en/signals/mt4/list/')
soup = BeautifulSoup(html.text, 'html.parser')

amountOfPages = int(soup.find(class_="paginatorEx").findAll('a')[-1].text)

for pageNumber in range(1, amountOfPages):
    print('## Page: ' + str(pageNumber))
    requestedHtml = requests.get('https://www.mql5.com/en/signals/mt4/list/page' + str(pageNumber))
    pageSoup = BeautifulSoup(requestedHtml.text, 'html.parser')

    page = pageSoup.find(class_="signals-table")
    list = page.findAll(class_="row signal")


    for signal in list:
        name = signal.find('span', { 'class' : 'name' }).text
        price = signal.find('div', { 'class' : 'col-price' }).text ##.replace('USD', '')
        growth = signal.find('div', { 'class' : 'col-growth' }).text
        monthGrowth = signal.find('div', { 'class' : 'col-growth' }).get('title', 'no title')
        subs = signal.find('div', { 'class' : 'col-subscribers' }).text
        funds = signal.find('div', { 'class' : 'col-facilities' }).text
        weeks = signal.find('div', { 'class' : 'col-weeks' }).text
        trades = signal.find('div', { 'class' : 'col-trades' }).text
        winrate = signal.find('div', { 'class' : 'col-plus' }).text
        dd = signal.find('div', { 'class' : 'col-drawdown' }).text
        link = signal.find('a', { 'class' : 'signal-avatar'}).get('href', '#')
        
        detailHtml = requests.get(link + '#!tab=stats')
        detailSoup = BeautifulSoup(detailHtml.text, 'html.parser')

        statistics = detailSoup.find('div', { 'id' : 'tradeDataColumns' })

        avgHolding = statistics.find('div', { 'title' : 'Average time of holding an open position' }).find(class_='s-data-columns__value').text
        tradesPerWeek = statistics.find('div', { 'title' : 'Average number of trades on signal\'s account for 7 days' }).find(class_='s-data-columns__value').text
        
        print(name)
        f.writerow([name, price, growth, monthGrowth, subs, funds, weeks, trades, winrate, dd])