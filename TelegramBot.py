#! /usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater
import time
from telegram.ext import CommandHandler
import random
import math

phrases = [
    "Что успел сегодня сделать?",
    "Как идут дела?",
    "Сегодня ты должен быть лучше, чем вчера",
    "Чем занимаешься?"
]

myDate = 870912000  # My birthday unix_time

def getCurrentTime():
    current_time = str(time.time())
    current_time = int(math.floor(float(current_time)))
    temp = current_time + 10800
    return int(temp)

def myDate():
    return int(870912000)

def deltaMyDate():
    response = getCurrentTime() - myDate()
    return response

def getYears():
    response = deltaMyDate() // 31536000
    return response

def getDays():
    response = deltaMyDate() % 31536000
    response = response // 86400
    return response

def getLeftDays():
    response = deltaMyDate() % 31536000
    response = response // 86400
    response = 365 - response
    return response

def getMonth():
    response = deltaMyDate() % 31536000
    response = response // 2592000
    return response

def getHours():
    response = deltaMyDate() % 31536000
    response = response % 86400
    response = response // 3600
    return response

def randHour():
    return random.randint(9, 22)

REQUEST_KWARGS={
    'proxy_url': 'http://104.248.118.217:8080/'
}
TOKEN = '745812568:AAH2SKlnxAqTaFuaIa9kZMb9IMsNLEgMCX4'
updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

print('"Time is going" is started')

def start(bot, update):
    rand_hour = randHour()
    currentDay = getDays()
    onoff = True
    while True:
        time.sleep(5)
        currentHour = getHours()
        if(currentDay != getDays()):
            onoff = True
        if(int(currentHour) == int(rand_hour) and onoff == True):

            print(vars(bot))
            rand_val = random.randint(0,3)
            print(rand_val)
            try:
                bot.send_photo(chat_id=278145396, photo='https://picsum.photos/200/300/?image='+str(random.randint(1, 1000)))
            except Exception:
                print(5)
            bot.send_message(chat_id=278145396, text=""+str(phrases[int(rand_val)])+"\n\nСегодня тебе: \n— "+str(getYears())+" год\n— "+str(getMonth())+" месяцев \n— "+str(getDays())+" дней\n\nДо дня рождения осталось: "+str(getLeftDays())+" дней")
            rand_hour = randHour()
            print("Message send!")
            onoff = False

def stop_the_messages(bot, update):
    bot.send_message(chat_id=278145396, text="Выключил бота")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
