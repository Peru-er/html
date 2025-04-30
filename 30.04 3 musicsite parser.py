
import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

songs = []

for item in soup.select('li.o-chart-results-list__item h3'):
    title = item.get_text(strip=True)
    artist = item.find_next('span')
    if title and artist:
        songs.append(f"{title} - {artist.get_text(strip=True)}")

with open("songs.txt", "w", encoding="utf-8") as f:
    for song in songs:
        f.write(song + "\n")

