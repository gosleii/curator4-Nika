import telebot
bot = telebot.TeleBot("1125811332:AAGMQFHCEHV1Lswxr7aodPbgpyhVkQXVP6k")
@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id,"Hello! You can find out:*band line-up,song list,concert dates*")
@bot.message_handler(commands=["band-line-up"])
def main(message):
    bot.send_message(message.chat.id,"Vocal,bass - *Chris*; Lead-guitar - *Nicky*; Rhythm-guitar - *Anthony*; Drums - *Fork*")
@bot.message_handler(commands=["concert-dates"])
def main(message):
    bot.send_message(message.chat.id,"10 December - *Bands Battle*; 16 December - *concert in Michurinsk*; 24 December - *Metal concert*")
bot.infinity_polling()