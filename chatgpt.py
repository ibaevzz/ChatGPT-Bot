import openai
import telebot
import urllib.request
from telebot import types

token = "YOUR TELEGRAM BOT TOKEN"
API_KEY = "YOUR OPENAI TOKEN"

openai.api_key = API_KEY
bot=telebot.TeleBot(token)

@bot.message_handler(commands=['image'])
def image_message(message):
    i = 1
    if message.text[7]>'0' and message.text[7]<='9':
        i = int(message.text[7])
    image_url = openai.Image.create(
        prompt=message.text,
        n=i,
        size="1024x1024")
    mass = []
    ii = 0
    while ii<i:
        mass.append(telebot.types.InputMediaPhoto(image_url.data[ii].url))
        ii=ii+1
    bot.send_media_group(message.chat.id, mass)

@bot.message_handler(content_types='text')
def start_message(message):
    MASS = message.text.split(" ")
    i = MASS[0].lower()
    ii = 0
    while ii<len(MASS):
        iii = MASS[ii].lower()
        if iii=="зубай":
            bot.send_message(message.chat.id,"че Зубай")
            return
        ii=ii+1
    
    mass = ["бот"]
    if not i in mass:
        return
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": message.text}])
    bot.send_message(message.chat.id,completion.choices[0].message.content)
        

bot.infinity_polling()


