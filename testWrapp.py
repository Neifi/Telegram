import telebot
import urllib.request
import sys
from bs4 import BeautifulSoup


def getData():
    data = urllib.request.urlopen('https://www.test.com',"html.parser").read().decode()
    soup = BeautifulSoup(data)
    tags = soup('span')
    

    for tag in tags:
        tags.encode('utf8')
        print(tag.get('href'))


getData()
