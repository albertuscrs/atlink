import sys, signal
import time
from datetime import datetime
import telebot
import logging

def signal_handler(signal, frame):
    #Ctrl+C to end the python session
    print("\nProgram exiting gracefully\nHave a nice Day! :)")
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

print('Bot Running...')
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
now = datetime.now()
TOKEN = AAA #from envi
bot = telebot.TeleBot(token=TOKEN)

def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, 'Booted up!')

@bot.message_handler(commands=['hello']) # welcome message handler
def send_welcome(message):
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    hi_msg = 'Hi There! Generate at '+date_time
    bot.reply_to(message, hi_msg)

@bot.message_handler(commands=['help']) # help message handler
def send_welcome(message):
    bot.reply_to(message, 'Still in progress!')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
# lambda function finds messages with the '@' sign in them
# in case msg.text doesn't exist, the handler doesn't process it
def at_converter(message):
    texts = message.text.split()
    at_text = findat(texts)
    if at_text == '@': # in case it's just the '@', skip
        pass
    else:
        insta_link = "https://instagram.com/{}".format(at_text[1:])
        bot.reply_to(message, insta_link)

while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        skr = datetime.now()
        date_time = skr.strftime("%m/%d/%Y, %H:%M:%S")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nTIMEOUT! DIULANG LAGI DI "+date_time+"\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        time.sleep(21)

# # while True:
# try:
#     while True:
#         bot.polling(none_stop=True)
#     # ConnectionError and ReadTimeout because of possible timout of the requests library
#     # maybe there are others, therefore Exception
# # except Exception:
# #     time.sleep(15)
# except KeyboardInterrupt:
#     print('interrupted!')
# # signal.signal(signal.SIGINT, signal_handler)