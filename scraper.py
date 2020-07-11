import csv

filename = 'signals.csv'

f = csv.writer(open(filename, 'w', newline=''))
f.writerow(['Name', 'Price', 'Growth', 'Monthly Growth', 'Subs', 'Funds', 'Weeks', 'Trades', 'Winrate', 'DD'])