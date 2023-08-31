import telebot
from telebot import types

# Create a new bot instance
bot = telebot.TeleBot('6599981531:AAHut2RrDP_rpG-uVhm9Wwo0wj7T3NTt80A')

# Define the handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    # Create the keyboard with the four buttons
    keyboard = types.InlineKeyboardMarkup()
    breakfast_button = types.InlineKeyboardButton("Чё на завтрак", callback_data='breakfast')
    lunch_button = types.InlineKeyboardButton("Чё на обед", callback_data='lunch')
    dinner_button = types.InlineKeyboardButton("Чё на ужин", callback_data='dinner')
    snack_button = types.InlineKeyboardButton("Чё перекусить", callback_data='snack')
    keyboard.row(breakfast_button)
    keyboard.row(lunch_button)
    keyboard.row(dinner_button)
    keyboard.row(snack_button)

    # Send the message with the keyboard
    bot.send_message(message.chat.id, 'Please choose an option:', reply_markup=keyboard)

# Define the callback query handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'breakfast':
        bot.send_message(call.message.chat.id, "You selected: Чё на завтрак")
    elif call.data == 'lunch':
        bot.send_message(call.message.chat.id, "You selected: Чё на обед")
    elif call.data == 'dinner':
        bot.send_message(call.message.chat.id, "You selected: Чё на ужин")
    elif call.data == 'snack':
        bot.send_message(call.message.chat.id, "You selected: Чё перекусить")

# Start the bot
bot.polling()
