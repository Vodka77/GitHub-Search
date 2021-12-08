import telebot 
import requests
import random 
import vodka
from telebot import types
from time import sleep
import time
import os,sys
def vodka(s):
 for ASU in s + '\n':
  sys.stdout.write(ASU)
  sys.stdout.flush()
  sleep(2./600)
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;32m'#اخضر
C = '\x1b[1;33m'#yellow
V = '\x1b[1;34m'#blue	
B = '\x1b[1;35m'#pink
N = '\x1b[1;36m'#لبني
M = '\x1b[1;37m'#ابيض	 
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
current_date =  time.strftime('%D', t)
vodka(X+'__     _____  ____  _  __    _    ')
vodka(Z+'\ \   / / _ \|  _ \| |/ /   / \   ')
vodka(X+' \ \ / / | | | | | |   /   / _ \  ')
vodka(Z+'  \ V /| |_| | |_| | . \  / ___ \ ')
vodka(X+'   \_/  \___/|____/|_|\_\/_/   \_\ ')
vodka(N+'Time Now : '+M+current_time)
vodka(N+'Date Now : '+M+current_date)
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Telegram : '+M+'@Vodka_tk')
vodka(Z+'('+X+'⌯'+Z+')'+N+'GitHub : '+M+'https://github.com/Vodkahunter.com')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program Code : '+M+'python3')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program App : '+M+'pycharm')
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
bot = telebot.TeleBot("5093213651:AAFOT-rhl_cwIuenm00OZDoxFBKyJ6bNn78")
py = types.InlineKeyboardButton(text ="- python",callback_data = 'python')
php = types.InlineKeyboardButton(text ="- php",callback_data = 'php')
java = types.InlineKeyboardButton(text ="- java",callback_data = 'java')
html = types.InlineKeyboardButton(text ="- Html",callback_data = 'html')
@bot.message_handler(commands=['start'])
def first(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(py,php,java,html)    
    bot.send_message(message.chat.id , f'<b>Hi VODKA #1st - python☬\n- - - - - - - - - - - - - -\nWelcome To GitHub Search\nClick The Lang Do You Want\n- - - - - - - - - - - - - -\nBy  : @Vodka_tk</b>', parse_mode="html",reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=(lambda message: True))
def message(message):
	if message.data == 'python':
         bot.send_message(chat_id=message.message.chat.id,text=f"<strong>- Wait Search Start . . . . .!</strong>",parse_mode="html")
         r = requests.get("https://apis.red/api/top-github/?lang=python").json()
         s1 = r['s1']['description']
         s11 = r['s1']['stars']	
         url = r['s1']['url']
         s2 = r['s2']['description']
         s22 = r['s2']['stars']
         url1 = r['s2']['url']
         s3 = r['s3']['description']
         s33 = r['s3']['stars']
         url2 = r['s3']['url']
         s4 = r['s4']['description']
         s44 = r['s4']['stars']
         url3 = r['s4']['url']
         s5 = r['s5']['description']
         s55 = r['s5']['stars']
         url4 = r['s5']['url']
         bot.send_message(chat_id=message.message.chat.id,text=f'<strong>Hi VODKA #1st - python☬ Done Swap Py\n- - - - - - - - - - - - -\n(1) - Description : {s1}\nStars : {s11}\nUrl : {url}\n(2) - Description : {s2}\nStars : {s22}\nUrl : {url1}\n(3) - Description : {s3}\nStars : {s33}\nUrl : {url}\nBY : @VODKA_Tk</strong>', parse_mode='html')
	elif message.data == 'php':
         bot.send_message(chat_id=message.message.chat.id,text=f"<strong>- Wait Search Start . . . . .!</strong>",parse_mode="html")
         r = requests.get("https://apis.red/api/top-github/?lang=php").json()
         s1 = r['s1']['description']
         s11 = r['s1']['stars']	
         url = r['s1']['url']
         s2 = r['s2']['description']
         s22 = r['s2']['stars']
         url1 = r['s2']['url']
         s3 = r['s3']['description']
         s33 = r['s3']['stars']
         url2 = r['s3']['url']
         s4 = r['s4']['description']
         s44 = r['s4']['stars']
         url3 = r['s4']['url']
         s5 = r['s5']['description']
         s55 = r['s5']['stars']
         url4 = r['s5']['url']
         bot.send_message(chat_id=message.message.chat.id,text=f'<strong>Hi VODKA #1st - python☬ Done Swap php\n- - - - - - - - - - - - -\n(1) - Description : {s1}\nStars : {s11}\nUrl : {url}\n(2) - Description : {s2}\nStars : {s22}\nUrl : {url1}\n(3) - Description : {s3}\nStars : {s33}\nUrl : {url}\nBY : @VODKA_Tk</strong>', parse_mode='html')  
	elif message.data == 'java':
         bot.send_message(chat_id=message.message.chat.id,text=f"<strong>- Wait Search Start . . . . .!</strong>",parse_mode="html")
         r = requests.get("https://apis.red/api/top-github/?lang=java").json()
         s1 = r['s1']['description']
         s11 = r['s1']['stars']	
         url = r['s1']['url']
         s2 = r['s2']['description']
         s22 = r['s2']['stars']
         url1 = r['s2']['url']
         s3 = r['s3']['description']
         s33 = r['s3']['stars']
         url2 = r['s3']['url']
         s4 = r['s4']['description']
         s44 = r['s4']['stars']
         url3 = r['s4']['url']
         s5 = r['s5']['description']
         s55 = r['s5']['stars']
         url4 = r['s5']['url']
         bot.send_message(chat_id=message.message.chat.id,text=f'<strong>Hi VODKA #1st - python☬ Done Swap java\n- - - - - - - - - - - - -\n(1) - Description : {s1}\nStars : {s11}\nUrl : {url}\n(2) - Description : {s2}\nStars : {s22}\nUrl : {url1}\n(3) - Description : {s3}\nStars : {s33}\nUrl : {url}\nBY : @VODKA_Tk</strong>', parse_mode='html')    	
	elif message.data == 'html':
         bot.send_message(chat_id=message.message.chat.id,text=f"<strong>- Wait Search Start . . . . .!</strong>",parse_mode="html")
         r = requests.get("https://apis.red/api/top-github/?lang=html").json()
         s1 = r['s1']['description']
         s11 = r['s1']['stars']	
         url = r['s1']['url']
         s2 = r['s2']['description']
         s22 = r['s2']['stars']
         url1 = r['s2']['url']
         s3 = r['s3']['description']
         s33 = r['s3']['stars']
         url2 = r['s3']['url']
         s4 = r['s4']['description']
         s44 = r['s4']['stars']
         url3 = r['s4']['url']
         s5 = r['s5']['description']
         s55 = r['s5']['stars']
         url4 = r['s5']['url']
         bot.send_message(chat_id=message.message.chat.id,text=f'<strong>Hi VODKA #1st - python☬ Done Swap html\n- - - - - - - - - - - - -\n(1) - Description : {s1}\nStars : {s11}\nUrl : {url}\n(2) - Description : {s2}\nStars : {s22}\nUrl : {url1}\n(3) - Description : {s3}\nStars : {s33}\nUrl : {url}\nBY : @VODKA_Tk</strong>', parse_mode='html')    		
pass
bot.polling(True)    				
    		    
