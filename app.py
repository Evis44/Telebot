from telegram.ext import Updater, MessageHandler,Filters

from Adafruit_IO import Client
import os

aio = Client('evis',os.getenv('evis'))
             
def demo1(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://i.pinimg.com/originals/3f/47/e0/3f47e02d05dc601d867771271a70c805.jpg'
  bot.message.reply_text('LIGHT is turned ON')
  aio.send('light', 1)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo2(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://cdn5.vectorstock.com/i/1000x1000/70/44/3d-realistic-off-light-bulb-icon-closeup-vector-27407044.jpg'
  bot.message.reply_text('LIGHT is turned OFF')
  aio.send('light', 0)
  data1 = aio.receive('light')
  print(f'Received value: {data1.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo3(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://thumbs.dreamstime.com/z/vintage-electric-fan-14689784.jpg'
  bot.message.reply_text('FAN is turned ON')
  aio.send('fan', 1)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def demo4(bot,update):
  chat_id = bot.message.chat_id
  path = 'https://c8.alamy.com/comp/DYE942/an-old-green-desk-fan-with-red-ribbons-against-a-white-background-DYE942.jpg'
  bot.message.reply_text('FAN is turned OFF')
  aio.send('fan', 0)
  data2 = aio.receive('fan')
  print(f'Received value: {data2.value}')
  update.bot.sendPhoto(chat_id=chat_id,photo=path)
def main(bot,update):
  a = bot.message.text.lower()
  print(a)

  if a =="lights on" or a=="turn on the light":
    demo1(bot,update)
  elif a =="lights off" or a=="turn off the light":
    demo2(bot,update)
  elif a =="switch on the fan" or a=="turn on fan":
    demo3(bot,update)
  elif a =="switch of the fan" or a=="turn off fan":
    demo4(bot,update)
  else:
    bot.message.reply_text('Invalid Text')
BOT_TOKEN = os.getenv('BOT_TOKEN')
u = Updater(BOT_TOKEN,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
