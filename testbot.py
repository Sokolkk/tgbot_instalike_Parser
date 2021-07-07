import telebot
import random


#Создаем новый TeleBot экземпляр, передав токен Telegram, который мы создали ранее
bot = telebot.TeleBot("ВашТокен")
rand = random.randint(1,111)

# вводим для начала диалога, /start
@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Привет! Я ваш первый бот!")

# Получаем случайное число, /number
@bot.message_handler(commands=['number'])
def handle_command(message):
    bot.reply_to(message, rand)

# все остальные сообщения  
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	bot.reply_to(message, "Извините, я не понял, что вы имеете в виду")

bot.polling()
#polling создает новый поток, который вызывает внутреннюю функцию для автоматического получения обновлений и передачи сообщений вашим обработчикам сообщений.
#Это функция блокировки, что означает, что коды ниже не будут выполняться. Обязательно поместите его в конец файла. 
#Также не вызывайте его более одного раза, иначе произойдет ошибка. 
