# -*- coding: utf-8 -*-
import telebot
bot = telebot.TeleBot("331309504:AAEsd-Ibit2bkvLH3fj0my1CXUxYgHp7A1Y")

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, u'Привет! Я SES_bot!')

@bot.message_handler()
def send_auth(message):
    msg = message.text;
    msg = msg.replace('s', 'ses')
    msg = msg.replace(u'с', u'сес')
    msg = msg.replace('S', 'SES')
    msg = msg.replace(u'С', u'СЕС')
    bot.reply_to(message, msg)
    print ">"*100 + "\n" + str(message.chat) + "\nwrote: " + message.text + "\nanswered: " + msg + "\n" + "<"*100

bot.polling()