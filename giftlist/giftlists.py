from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import ssl
ssl._create_default_https_context=ssl._create_unverified_context

def getimg(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print('url not found!!!')
    try:
        bs_obj = BeautifulSoup(html, features='html.parser')
        images = bs_obj.findAll('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})
    except AttributeError as e:
        print("image not found!!")

    return images


images = getimg('https://www.pythonscraping.com/pages/page3.html')

for image in images:
    print(image['src'])
