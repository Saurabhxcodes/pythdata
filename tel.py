'''from telegram import *
from telegram.ext import *
bot = Bot('5523942973:AAG5dV9pVrkmHxeyB_GdD-6OTIOMYt4Gjag')
print(bot.get_me())
updater=Updater('5523942973:AAG5dV9pVrkmHxeyB_GdD-6OTIOMYt4Gjag' ,use_context=True)
#use_context is use for if your telegram version is low than use false else use true
dispatcher=updater.dispatcher
# For Commands 
def test_fnc2(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="hey WELCOME in my WORLD ",
        )
start_value2=CommandHandler('start', test_fnc2)
dispatcher.add_handler (start_value2)

#adding more Command
def test_fnc(update: Update, context: CallbackContext):
    bot.send_message(
        chat_id=update.effective_chat.id,
        text="https://gaana.com/playlist/gaana-dj-bollywood-top-50-1"
        )
start_value=CommandHandler('songs', test_fnc)
dispatcher.add_handler (start_value)
updater.start_polling()'''