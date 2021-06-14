from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def buy_keyboard(item_id):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Купить биткоином', callback_data=f'buy_btc:{item_id}'),
                InlineKeyboardButton(text='Купить ефириумом', callback_data=f'buy_eth:{item_id}')
            ]
        ]
    )
    return keyboard


paid_keyboard_btc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Оплатил',
                callback_data='paid')
        ],
    ]
)

paid_keyboard_eth = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Оплатил',
                callback_data='paid_eth')
        ],
    ]
)
