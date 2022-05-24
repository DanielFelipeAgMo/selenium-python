from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re

tom = urlopen("https://es.wikipedia.org/wiki/Tom_Cruise")
soup = bs(tom.read())

for link in soup.find_all('a'):
    if 'href' in link.attrs:
        #print(link.get('href'))
        print(link.attrs['href'])


for link in soup.find('div',{'id':'bodyContent'}).findAll('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

"""for link in soup.find('div', {'id':'mw-content-text'}).find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])"""