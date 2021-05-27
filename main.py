from dateutil.parser import parse, ParserError
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
load_dotenv()

# -------------------------------- DATE PARSING --------------------------------- #
while True:
    date = input('Which year do you want to travel to? : ')
    try:
        date = parse(date).date()
        break
    except ParserError:
        print('Please give a valid date...')
        continue

# -------------------------------- BEAUTIFUL SOUP -------------------------------- #
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
html = response.text

soup = BeautifulSoup(html, 'html.parser')
titles = [title.getText() for title in soup.find_all(name='span', class_='chart-element__information__song')]

# ----------------------------------- SPOTIFY ----------------------------------- #
scope = "playlist-modify-public"
CLIENT_ID = os.environ.get('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIPY_CLIENT_SECRET')

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri='http://example.com',
        scope=scope,
        show_dialog=True
    )
)
user_id = sp.current_user()['id']

