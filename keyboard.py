from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_card_num_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    btn_arr = ['2', '3', '4', '5', '6', '7',
               '8', '9', '10', 'J', 'Q', 'K', 'A']
    for i in range(0, 11, 3):
        markup.add(InlineKeyboardButton(btn_arr[i], callback_data=btn_arr[i]),
                   InlineKeyboardButton(
                       btn_arr[i+1], callback_data=btn_arr[i+1]),
                   InlineKeyboardButton(
                       btn_arr[i+2], callback_data=btn_arr[i+2])
                   )
    markup.add(InlineKeyboardButton(btn_arr[12], callback_data=btn_arr[12]))
    return markup
