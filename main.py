from dateutil.parser import parse, ParserError
from bs4 import BeautifulSoup
import requests

while True:
    date = input('Which year do you want to travel to? : ')
    try:
        date = parse(date).date()
        break
    except ParserError:
        print('Please give a valid date...')
        continue

response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
html = response.text

soup = BeautifulSoup(html, 'html.parser')
titles = soup.find_all(name='span', class_='chart-element__information__song')

for i in titles:
    print(i.getText())
