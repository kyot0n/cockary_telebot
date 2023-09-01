from background import keep_alive
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
from telebot import types


# Create a new bot instance
bot = telebot.TeleBot('6599981531:AAHut2RrDP_rpG-uVhm9Wwo0wj7T3NTt80A')


# Define the handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    global old, CHAT_ID
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
    CHAT_ID = message.chat.id
    old = bot.send_message(message.chat.id, 'Выберите:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data in ['breakfast', 'lunch', 'dinner', 'snack'])
def start_choice(call):
    bot.delete_message(old.chat.id, old.message_id)
    if call.data == 'breakfast':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё на завтрак")
    elif call.data == 'lunch':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё на обед")
    elif call.data == 'dinner':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё на ужин")
    elif call.data == 'snack':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё перекусить")
    cuisine()


def cuisine():
    global old
    # Create the keyboard with the four buttons
    keyboard = types.InlineKeyboardMarkup()
    ru_button = types.InlineKeyboardButton("Русская кухня", callback_data='ru')
    usa_button = types.InlineKeyboardButton("Американская кухня", callback_data='usa')
    uk_button = types.InlineKeyboardButton("Английская кухня", callback_data='uk')
    fr_button = types.InlineKeyboardButton("Французская кухня", callback_data='fr')
    keyboard.row(ru_button)
    keyboard.row(usa_button)
    keyboard.row(uk_button)
    keyboard.row(fr_button)

    # Send the message with the keyboard
    old = bot.send_message(CHAT_ID, 'Выберите кухню:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data in ['ru', 'usa', 'uk', 'fr'])
def dish(call):
    bot.delete_message(old.chat.id, old.message_id)
    if call.data == 'ru':
        bot.send_message(call.message.chat.id, "Вы выбрали: RU")
    elif call.data == 'usa':
        bot.send_message(call.message.chat.id, "Вы выбрали: USA")
    elif call.data == 'uk':
        bot.send_message(call.message.chat.id, "Вы выбрали: UK")
    elif call.data == 'fr':
        bot.send_message(call.message.chat.id, "Вы выбрали: FR")


# Start the bot
keep_alive()
bot.polling(non_stop=True, interval=0)