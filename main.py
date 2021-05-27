from dateutil.parser import parse, ParserError
from bs4 import BeautifulSoup
import requests

while True:
    date = input('Which year do you want to travel to? Type the date in YYYY-MM-DD: ')
    try:
        date = parse(date).date()
        break
    except ParserError:
        print('Please give a valid date...')
        continue

print(date)
