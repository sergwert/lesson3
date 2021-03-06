# Установите модуль ephem
# Добавьте в бота команду /planet, которая будет принимать на вход название планеты на английском.
# При помощи условного оператора if и ephem.constellation научите бота отвечать, в каком созвездии сегодня находится планета.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
import ephem
import datetime
from key import tgrf_key

PROXY={'proxy_url': 'socks5://t1.learn.python.ru:1080', 'urllib3_proxy_kwargs': {'username':'learn', 'password':'python'}}
import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log')

def great_user(bot, update):
    text="Вызван /start"
    #print(text)
    update.message.reply_text(text)
    #print(update)

    
def ask_planet(bot, update):
    text="Введите название планеты на английском: "
    #print(text)
    update.message.reply_text(text)
    planet_constellation(bot,update)

def planet_constellation(bot, update):
    
    p_planet=update.message.text
    if p_planet.lower()=='mars':
        ret=ephem.constellation(ephem.Mars(datetime.datetime.now()))
    elif p_planet.lower()=='venus':
        ret=ephem.constellation(ephem.Venus(datetime.datetime.now()))
    elif p_planet.lower()=='jupiter':
        ret=ephem.constellation(ephem.Jupiter(datetime.datetime.now()))
    elif p_planet.lower()=='uranus':
        ret=ephem.constellation(ephem.Uranus(datetime.datetime.now()))
    elif p_planet.lower()=='neptune':
        ret=ephem.constellation(ephem.Neptune(datetime.datetime.now()))
    elif p_planet.lower()=='sun':
        ret=ephem.constellation(ephem.Sun(datetime.datetime.now()))
    elif p_planet.lower()=='moon':
        ret=ephem.constellation(ephem.Moon(datetime.datetime.now()))
    elif p_planet.lower()=='earth':
        ret=ephem.constellation(ephem.Earth(datetime.datetime.now()))
    elif p_planet.lower()=='mercury':
        ret=ephem.constellation(ephem.Mercury(datetime.datetime.now()))

    update.message.reply_text('Планета '+p_planet+' находится в созвездии '+ret[1])

def wordcount(bot, update):
    text=update.message.text
    word_arr=text.split(" ")
    wrd_cnt=-1
    for i in word_arr:
        wrd_cnt=wrd_cnt+1
    update.message.reply_text("Кол-во слов: "+str(wrd_cnt))

def talk_to_me(bot, update):
    user_text=update.message.text
    #print(user_text)
    update.message.reply_text(user_text)


def calc(bot, update):
    text=update.message.text.replace("/calc","").strip()
    # custom_keyboard = [['top-left', 'top-right'], ['bottom-left', 'bottom-right']]
    # reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    # bot.send_message(chat_id=chat_id, text="Custom Keyboard Test", reply_markup=reply_markup)
    if text.endswith("="):
        if "+" in text:
            sym_arr=text.replace("=","").split("+")
            val=int(sym_arr[0].strip())+int(sym_arr[1].strip())
        elif "*" in text:
            sym_arr=text.replace("=","").split("*")
            val=int(sym_arr[0].strip())*int(sym_arr[1].strip())
        elif "-" in text:
            sym_arr=text.replace("=","").split("-")
            val=int(sym_arr[0].strip())-int(sym_arr[1].strip())
        elif "/" in text:
            sym_arr=text.replace("=","").split("/")
            val=int(sym_arr[0].strip())/int(sym_arr[1].strip())

    update.message.reply_text("Результат: "+str(val))

def main():
    mybot=Updater(tgrf_key, request_kwargs=PROXY)
    dp=mybot.dispatcher
    dp.add_handler(CommandHandler("start", great_user))
    dp.add_handler(CommandHandler("planet", ask_planet))
    dp.add_handler(CommandHandler("wordcount", wordcount))
    dp.add_handler(CommandHandler("calc", calc))
    #dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(MessageHandler(Filters.text, planet_constellation))
    mybot.start_polling()
    mybot.idle()

main()