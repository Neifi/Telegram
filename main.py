import telebot
import urllib.request
import sys
from bs4 import BeautifulSoup


bot = telebot.TeleBot("964319736:AAHFO478jpHvTY1Jnp1Nadxqb-GpR9a314A")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(
        message, "Hi type /search and search what you want: E; /search Gaming monitor ")


@bot.message_handler(commands=['search'])
def find(message):

    word = message.text[7:]
    link = "https://www.google.com/search?q="+word+"&safe=strict&hl"
    +"=es&tbm=shop&sxsrf=ACYBGNS2RQ9jixBcnsdeqonfJ3KwkkSd7Q:"
    +"1570631053274&tbs=p_ord:p&ei"
    
    

bot.polling()


def getData(link):
    data = urllib.request.urlopen(link).read().decode()
    dataSoup = BeautifulSoup(data)
    dataTags = dataSoup('a')
    for tag in dataTags:
        print(tag.get('href'))

    
