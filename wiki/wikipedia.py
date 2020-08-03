from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

random.seed(datetime.datetime.now())
def getlinks(articalUrl):
    html = urlopen('http://en.wikipedia.org'+articalUrl)
    bs_obj = BeautifulSoup(html, 'html.parser')
    return bs_obj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))
links=getlinks('/wiki/Kevin_Bacon')
while 1:
    newAartical=links[random.randint(0,len(links)-1)].attrs['href']
    print(newAartical)
    links=getlinks(newAartical)
# for link in bs_obj.find():
#
#     if 'href' in link.attrs:
#         print(link.attrs['href'])
