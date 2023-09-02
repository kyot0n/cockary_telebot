from background import keep_alive
import pip
pip.main(['install', 'pytelegrambotapi'])
import telebot
from telebot import types


# Create a new bot instance
bot = telebot.TeleBot('6599981531:AAHut2RrDP_rpG-uVhm9Wwo0wj7T3NTt80A')

# Global variables that user inputs
time, cuisine, dish = None, None, None

# Define the handler for the /start command
# Time selection function
@bot.message_handler(commands=['start'])
def start(message):
    # Old message that bot sends, chat ID
    global old, CHAT_ID
    CHAT_ID = message.chat.id
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
    old = bot.send_message(message.chat.id, 'Выберите:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data in ['breakfast', 'lunch', 'dinner', 'snack'])
def start_choice(call):
    global time
    # Delete last message from bot
    bot.delete_message(old.chat.id, old.message_id)

    if call.data == 'breakfast':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё на завтрак")
        time = 'breakfast'
    elif call.data == 'lunch':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё на обед")
        time = 'lunch'
    elif call.data == 'dinner':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё на ужин")
        time = 'dinner'
    elif call.data == 'snack':
        bot.send_message(call.message.chat.id, "Вы выбрали: Чё перекусить")
        time = 'snack'

    cuisine()

# Cusine selection function
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
def cuisine_choice(call):
    global cuisine
    # Delete last message from bot
    bot.delete_message(old.chat.id, old.message_id)

    if call.data == 'ru':
        bot.send_message(call.message.chat.id, "Вы выбрали: Русскую кухню")
        cuisine = 'ru'
    elif call.data == 'usa':
        bot.send_message(call.message.chat.id, "Вы выбрали: Американскую кухню")
        cuisine = 'usa'
    elif call.data == 'uk':
        bot.send_message(call.message.chat.id, "Вы выбрали: Английская кухню")
        cuisine = 'uk'
    elif call.data == 'fr':
        bot.send_message(call.message.chat.id, "Вы выбрали: Французскую кухню")
        cuisine = 'fr'

    dish()


# Dish selection function
def dish():
    global old
    # Create the keyboard with the four buttons
    keyboard = types.InlineKeyboardMarkup()
    d1_button = types.InlineKeyboardButton("БЛЮДО1", callback_data='dish1')
    d2_button = types.InlineKeyboardButton("БЛЮДО2", callback_data='dish2')
    d3_button = types.InlineKeyboardButton("БЛЮДО3", callback_data='dish3')
    d4_button = types.InlineKeyboardButton("БЛЮДО4", callback_data='dish4')
    keyboard.row(d1_button)
    keyboard.row(d2_button)
    keyboard.row(d3_button)
    keyboard.row(d4_button)

    # Send the message with the keyboard
    old = bot.send_message(CHAT_ID, 'Выберите блюдо:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda callback: callback.data in ['dish1', 'dish2', 'dish3', 'dish4'])
def dish_choice(call):
    global old, time, cuisine, dish
    dish = call.data
    # Delete last message from bot
    bot.delete_message(old.chat.id, old.message_id)

    # {FOR DEVELOPMENT} Send message with selected data
    bot.send_message(CHAT_ID, f"{time}, {cuisine}, {dish}")


# Start the bot
keep_alive()
bot.polling(non_stop=True, interval=0)
