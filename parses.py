import requests
from bs4 import BeautifulSoup

def suck(a,b,c):
    url = str(a)

    source = requests.get(url)
    main_text = source.text
    soup = BeautifulSoup(main_text, "html.parser")

    link = soup.find(str(b), {'class': str(c)})

    return link.text
suck('https://www.hltv.org/', 'a', 'navgalleries')
