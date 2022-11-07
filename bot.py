import subprocess
import telebot
from telebot import custom_filters

bot = telebot.TeleBot("TOKEN")

command1 = "echo hello world"
command2 = "echo hello from other server"
chatid = CHATID

@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "Yo, how can i help you?")

@bot.message_handler(chat_id=[chatid], commands=['TELEGRAM_COMMAND_1'])
def command1_result(message):
    run_command = subprocess.Popen(command1, shell=True, stdout=subprocess.PIPE).stdout.read()
    bot.send_message(message.chat.id, run_command)

@bot.message_handler(chat_id=[chatid], commands=['TELEGRAM_COMMAND_2'])
def command2_result(message):
    command = ["sshpass", "-p", "PASSWORD", "ssh", "USER" + "@" + 
"SERVER", command2]
    run_command = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.read()
    bot.send_message(message.chat.id, run_command)

@bot.message_handler(commands=['TELEGRAM_COMMAND_1'])
def ds_status_denied(message):
    bot.send_message(message.chat.id, "You are not allowed to use this command")

@bot.message_handler(commands=['TELEGRAM_COMMAND_2'])
def ds_status_denied(message):
    bot.send_message(message.chat.id, "You are not allowed to use this command")


bot.add_custom_filter(custom_filters.ChatFilter())
bot.infinity_polling()
