### Description
A scraper for mql5 signals that exports the data into a csv.

You may get 403 from mql5 server if you run this script due to number of requests per second, so one may want to add a delay.

### Dependencies

- requests
- BeautifulSoup
- csv

### Requirements
- Python 3.7

### Run

```
python3 -m venv env

source env/bin/activate

pip install requests

pip install beautifulsoup4

python3 scraper.py

```

