import requests
from bs4 import BeautifulSoup as BS

r=requests.get('https://stopgame.ru/news')
html=BS(r.content,'html.parser')

for el in html.select('.items > .article-summary'):
    tit=el.select('.caption > a')
    print(tit[0].text)
