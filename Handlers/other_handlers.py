from aiogram import Router, Bot, F
# from aiogram.types import Message
from aiogram.types import Message, ReplyKeyboardMarkup, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import CommandStart
# from aiogram.filters import CommandStart, Text
from Keyboards.keyboards import create_key, create_inline_key
# from Lexicon import lexicon
from Lexicon.lexicon import LEXICON_MENU, LEXICON_INLINE, main_buttons, labels, choosen_label, probabilities

# from telegram import ReplyKeyboardRemove
import time

# from Param.const import pathes
from Param import const
from Lexicon import nn

# global keyboard_inline
global msg

# print(const.pathes)

router: Router = Router()


# keyboard_start = create_key(2, **LEXICON_MENU)
# keyboard_inline = create_inline_key(2, **LEXICON_INLINE)

# keyboard_inline = create_inline_key(1, **buttons)   # Если buttons - это словарь
# keyboard_inline = create_inline_key(1, *button_data)


@router.message(CommandStart())
async def process_start_command(message: Message):
    print(f'1message.from_user.id={message.from_user.id}')
    # print(f'1callback.from_user.id={callback.from_user.id}')
    # await message.answer('Hi!', reply_markup=keyboard_start)
    await message.answer("Hi! Send me a photo and I'll try to classify it!")
    print(f'2message.from_user.id={message.from_user.id}')
    # print(f'callback.from_user.id={callback.from_user.id}')






# @dp.message(F.photo)  # Handle photo messages
@router.message(F.photo)  # Handle photo messages
async def download_photo(message: Message, bot: Bot):
    print(f'1 type of message.from_user.id={type(message.from_user.id)}')
    cur_user_id = message.from_user.id
    # print(f'1callback.from_user.id={callback.from_user.id}')
    # lbls: list[str] = []
    # nonlocal lbls, probabilities
    # Download the photo
    try:
        pass
        # await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id)
    except:
        pass

    # Download the photo
    file_photo_pth_in = f"{const.pathes['photo_pth_in']}{message.photo[-1].file_id}.jpg"
    await bot.download(
        message.photo[-1],
        # destination=f"{const.pathes['photo_pth_in']}{message.photo[-1].file_id}.jpg"
        destination=file_photo_pth_in
    )

    #     # Пример использования load_img
    #     # img = load_img('image.jpg', target_size=(224, 224))
    #     # img = load_img(f"/tmp/{message.photo[-1].file_id}.jpg", target_size=(224, 224))# Так работает
    # main_buttons[0] = 'lj'
    # lalabels[0] = 'lj'
    lbls, probs = nn.get_predicts(file_photo_pth_in)
    # labels, probabilities = nn.get_predicts(file_photo_pth_in)
    # print(f'len(lbls)={len(lbls)}')
    # print(f'len(probs)={len(probs)}')
    # print(labels)
    # print(probabilities)

    # for i in range(len(lbls)):
    #     labels[i] = lbls[i]
    #     probabilities[i] = probs[i]

    # labels[cur_user_id] = lbls
    # probabilities[cur_user_id] = probs
    labels.update({cur_user_id: lbls})
    probabilities.update({cur_user_id: probs})

    # labels1, probabilities1 = nn.get_predicts(file_photo_pth_in)
    # for i in range(3):
    #     lbls[i] = labels1[i]
    #     probabilities[i] = probabilities1[i]
    # for i in range(3):
    #     main_buttons[i] = f'"{labels[i]}", p={probabilities[i] * 100:.0f}%'
    #     print(f'labels[{i}]={labels[i]}, probabilities[{i}]={probabilities[i]}')
    # main_buttons.update({cur_user_id: [f'"{label}", p={prob * 100:.0f}%' for label, prob in zip(labels.values(), probabilities.values())]})
    # main_buttons.update({cur_user_id: [f'"{label}", p={prob}' for label, prob in zip(labels.values(), str.probabilities.values())]})
    main_buttons.update({cur_user_id: [f'"{label}", p={prob * 100:.0f}%' for label, prob in zip(labels[cur_user_id], probabilities[cur_user_id])]})
    print(f'labels={labels}')
    print(f'probabilities={probabilities}')
    print(f'main_buttons[cur_user_id] = {main_buttons[cur_user_id]}')

    # button_data[0] = 'abc'
    # for key, value in zip(buttons.keys(), button_data):
    #     buttons[key] = value
    #
    # keyboard_inline = create_inline_key(1, **buttons)  # Если buttons - это словарь
    # keyboard_inline = create_inline_key(1, *(main_buttons[cur_user_id]), button1='Choose from the list', button2='New photo')  # Если main_buttons - это список
    keyboard_inline = create_inline_key(1, *(main_buttons[cur_user_id]), choose_from_the_list='Choose from the list', new_photo='New photo')  # Если main_buttons - это список
    # keyboard_inline2 = create_inline_key(2, *alt_buttons)  # Если alt_buttons - это список

    # button_data0 = f'"{lbls[0]}", p={probabilities[0] * 100:.0f}%'
    # buttons = {
    #     'But0': f'"{lbls[0]}", p={probabilities[0] * 100:.0f}%',
    #     'But1': f'"{lbls[1]}", p={probabilities[1] * 100:.0f}%',
    #     'But2': f'"{lbls[2]}", p={probabilities[2] * 100:.0f}%'
    # }

    await bot.send_message(message.from_user.id, 'Choose the right button', reply_markup=keyboard_inline)

    # bot.send_message(chat_id=chat_id, text="Клавиатура была удалена.", reply_markup=ReplyKeyboardRemove())
    # await bot.send_message(message.chat.id, text="Клавиатура была удалена.", reply_markup=ReplyKeyboardRemove())

    # Удаление ненужных инлайн-клавиатур (и, наверное, не только их)
    # await bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
    # await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 1)
    # await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id - 2)
    print(f'2message.from_user.id={message.from_user.id}')
    # print(f'callback.from_user.id={callback.from_user.id}')


# @router.message(Text(text='Hi Bot!')) # Так не работает
@router.message(F.text == 'Hi Bot!')
async def hi(message: Message, bot: Bot):
    print(f'1message.from_user.id={message.from_user.id}')
    # print(f'callback.from_user.id={callback.from_user.id}')
    await bot.send_message(message.from_user.id, 'Hi user!')
    print(f'2message.from_user.id={message.from_user.id}')
    # print(f'callback.from_user.id={callback.from_user.id}')

    # @router.message(Text(text='First But'))
    print(f'2message.from_user.id={message.from_user.id}')
    # print(f'callback.from_user.id={callback.from_user.id}')


@router.message(F.text == 'First But')
async def but1(message: Message, bot: Bot):
    # await bot.send_message(message.from_user.id, 'Hi user!')
    await bot.send_message(message.from_user.id, 'Первая кнопка!', reply_markup=keyboard_inline)


@router.message(F.text)
async def any_txt(message: Message, bot: Bot):
    print(f'1message.from_user.id={message.from_user.id}')
    # print(f'callback.from_user.id={callback.from_user.id}')
    await bot.send_message(message.from_user.id, 'Hi hi!')
    print(f'2message.from_user.id={message.from_user.id}')
    # print(f'callback.from_user.id={callback.from_user.id}')


# @router.callback_query(F.data == 'Nobe1')
# async def but1(callback: CallbackQuery):
#     # await callback.message.answer('Нажали первую кнопку!', reply_markup=keyboard_inline)
#     # await callback.message.answer(str(randint(1, 10)))
#     # await callback.answer('Нажали кнопку 1')    # Выводит сообщение вверху экрана секунды на три
#     # Далее - сообщение над инлайн-клавиатурой и снова запуск инлайн клавиатуры,
#     # но, если дважды нажать на первую кнопку инлайн-клавиатуры,  то будет ошибка (бот продолжит работать),
#     # т.к. редактировать без изменения текста - это ошибка.
#     try:
#         await callback.message.edit_text('Нажали кнопку 1', reply_markup=keyboard_inline)
#     except:
#         await callback.answer('УЖЕ нажали САМУЮ первую кнопку!')

# ЕСЛИ ВЫБРАЛИ ОДНУ ИЗ ТРЕХ КНОПОК-КЛАССОВ
# @router.callback_query(lambda callback_query: True)
# @router.callback_query(lambda c: c.data == main_buttons[0])
# @router.callback_query(lambda c: c.data in main_buttons[c.from_user.id]) # Так не работает
@router.callback_query(lambda c: c.data in [item for sublist in main_buttons.values() for item in sublist])
async def main_but0(callback: CallbackQuery, bot: Bot):
    print(f'main_buttons={main_buttons}')
    # print(f'message.from_user.id={message.from_user.id}')
    print(f'1callback.from_user.id={callback.from_user.id}')
    # for a in [callback.data, callback.message, callback.inline_message_id, callback.id, callback.from_user, callback.chat_instance]:
    #     print(f'{a}')
    await callback.message.delete()  # А так удаляются и инлайн клавиатура (кнопки), и сообщение.
    tmp_butts = []
    keyboard_inline = create_inline_key(1, *tmp_butts, choose_confirm='Confirm your choice',
                                        choose_goback='Go back')  # Если main_buttons - это список
    # await bot.send_message(message.from_user.id, 'Choose the right button.', reply_markup=keyboard_inline)
    # await bot.send_message(callback.from_user.id, 'Choose the right button.', reply_markup=keyboard_inline)
    # await bot.send_message(callback.from_user.id, main_buttons[0], reply_markup=keyboard_inline)
    if callback.data in main_buttons[callback.from_user.id]:
        print('OK: callback.data in main_buttons[callback.from_user.id]')
    else:
        print('!!! ОШИБКА !!! НЕ ВЫПОЛНЯЕТСЯ callback.data in main_buttons[callback.from_user.id]')

    for i in range(3):
        if callback.data == main_buttons[callback.from_user.id][i]:
            choosen_label[callback.from_user.id] = labels[callback.from_user.id][i]
            await bot.send_message(callback.from_user.id, labels[callback.from_user.id][i], reply_markup=keyboard_inline)

    # if callback.data == main_buttons[0]:
    #     await bot.send_message(callback.from_user.id, labels[0], reply_markup=keyboard_inline)
    # elif callback.data == main_buttons[1]:
    #     await bot.send_message(callback.from_user.id, labels[1], reply_markup=keyboard_inline)
    # elif callback.data == main_buttons[2]:
    #     await bot.send_message(callback.from_user.id, labels[2], reply_markup=keyboard_inline)
    # print(f'message.from_user.id={message.from_user.id}')
    print(f'2callback.from_user.id={callback.from_user.id}')

# ДАЛЕЕ ОБРАБОТАТЬ КНОПКИ 'Confirm your choice' и 'Go back' С УЧЕТОМ menu_level !!!!!!!!!!!!!!!!!!!!!
# ПРИ ВЫБОРЕ КНОПКИ 'Confirm your choice' НУЖНО УДАЛИТЬ ИЗ main_buttons ЗАПИСЬ С КЛЮЧЕМ callback.from_user.id !!!!!!!!!!!!!!!!!!!!!
# ЧТОБЫ НЕ ХРАНИТЬ В main_buttons МУСОР

# ЕСЛИ ВЫБРАЛИ КНОПКУ ПОДТВЕРЖДЕНИЯ ВЫБРАННОГО КЛАССА
@router.callback_query(F.data == 'choose_confirm')
# async def ch_confirm(callback: CallbackQuery, bot: Bot):
async def ch_confirm(callback: CallbackQuery):
    # print(f'message.from_user.id={message.from_user.id}')
    print(f'1callback.from_user.id={callback.from_user.id}')
    # Здесь сохраняем файл-фотографию в нужной директории
    # и обнуляем labels, probabilities и main_buttons? - похоже да.
    await callback.message.edit_reply_markup()    # Так удаляется инлайн клавиатура (кнопки), но сообщение остается.
    # await callback.message.delete()  # А так удаляются и инлайн клавиатура (кнопки), и сообщение.
    # print(f'message.from_user.id={message.from_user.id}')
    print(f'2callback.from_user.id={callback.from_user.id}')
    # await bot.send_message(message.from_user.id, 'Hi user!')
    await callback.message.answer(f'Подтвержден класс "{choosen_label[callback.from_user.id]}"')
    # Далее нужно записать файл-фотографию в каталог с именем choosen_label[callback.from_user.id]
    # и удалить main_buttons[callback.from_user.id], labels[callback.from_user.id] и probabilities[callback.from_user.id]

# ЕСЛИ ВЫБРАЛИ КНОПКУ ВОЗВРАТА ПОСЛЕ ВЫБОРА КЛАССА
@router.callback_query(F.data == 'choose_goback')
# async def ch_goback(message: Message, callback: CallbackQuery, bot: Bot):
async def ch_goback(callback: CallbackQuery, bot: Bot):
    # print(f'message.from_user.id={message.from_user.id}')
    print(f'1callback.from_user.id={callback.from_user.id}')
    # Возвращаемся к главному меню - выбору класса
    # await callback.message.edit_reply_markup()    # Так удаляется инлайн клавиатура (кнопки), но сообщение остается.
    await callback.message.delete()  # А так удаляются и инлайн клавиатура (кнопки), и сообщение.
    keyboard_inline = create_inline_key(1, *(main_buttons[callback.from_user.id]), button1='Choose from the list', button2='New photo')  # Если main_buttons - это список
    await bot.send_message(callback.from_user.id, 'Choose the right button', reply_markup=keyboard_inline)

# ЕСЛИ ВЫБРАЛИ КНОПКУ 'New photo'
@router.callback_query(F.data == 'new_photo')
# async def new_photo(callback: CallbackQuery, bot: Bot):
async def new_photo(callback: CallbackQuery):
    await callback.message.edit_reply_markup()    # Так удаляется инлайн клавиатура (кнопки), но сообщение остается.
    # await callback.message.delete()  # А так удаляются и инлайн клавиатура (кнопки), и сообщение.
    await callback.message.answer("Send me a photo and I'll try to classify it!")


# Далее не используется
# @router.callback_query(lambda c: True)
@router.callback_query(lambda c: False)
# @router.callback_query(callback_data == main_buttons[0])
# @router.callback_query(F.data == 'abc')
# async def but0(callback: CallbackQuery, message: Message, bot: Bot) -> object:
# async def but0(callback: CallbackQuery, bot: Bot, message: Message):
async def but0(callback: CallbackQuery, bot: Bot):
# async def but0(callback: CallbackQuery):
# async def but0(message: Message, callback: CallbackQuery):
# async def but0(message: Message):
# async def but0():
    # await callback.message.answer('Нажали первую кнопку!', reply_markup=keyboard_inline)
    # await callback.message.answer(str(randint(1, 10)))
    # await callback.answer('Нажали кнопку 1')    # Выводит сообщение вверху экрана секунды на три
    # Далее - сообщение над инлайн-клавиатурой и снова запуск инлайн клавиатуры,
    # но, если дважды нажать на первую кнопку инлайн-клавиатуры,  то будет ошибка (бот продолжит работать),
    # т.к. редактировать без изменения текста - это ошибка.
    # await callback.message.edit_reply_markup()    # Так удаляется инлайн клавиатура (кнопки), но сообщение остается.
    # print(f'button_data={button_data}')
    # await bot.send_message(message.from_user.id, 'Choose the right button.', reply_markup=keyboard_inline)
    print(f'callback.data={callback.data}')
    print(f'main_buttons={main_buttons}')
    print(f'callback.inline_message_id={callback.inline_message_id}')
    if callback.data == main_buttons[0]:
        await callback.message.delete()                 # А так удаляются и инлайн клавиатура (кнопки), и сообщение.
    elif callback.data == main_buttons[1]:
        # pass
        print('main_buttons[1]')
        # buttons2 = ['ok']
        buttons2 = []
        keyboard_inline = create_inline_key(1, *buttons2, button1='Choose from the list',
                                            button2='New photo')  # Если main_buttons - это список
        # await bot.send_message(message.from_user.id, 'Choose the right button.', reply_markup=keyboard_inline)
        await bot.send_message(callback.from_user.id, 'Choose the right button.', reply_markup=keyboard_inline)
        await bot.answer_callback_query(callback.id)
    elif callback.data == main_buttons[2]:
        pass
    elif callback.data == 'button1':
        # print(0)
        pass
    elif callback.data == 'button2':
        # print(1)
        pass



    # try:
    #     # await callback.message.edit_text(f'"{labels[0]}", p={probabilities[0] * 100:.0f}%',
    #     await callback.message.edit_text(button_data[0], reply_markup=keyboard_inline)
    #
    # except:
    #     await callback.answer('УЖЕ нажали САМУЮ первую кнопку!')


@router.callback_query(F.data == 'Nobe1')
async def but1(callback: CallbackQuery):
    await callback.message.answer('Нажали первую кнопку!', reply_markup=keyboard_inline)
    # await callback.message.answer(str(randint(1, 10)))
    await callback.answer('Нажали кнопку 1')  # Выводит сообщение вверху экрана секунды на три
    # Далее - сообщение над инлайн-клавиатурой и снова запуск инлайн клавиатуры
    try:
        await callback.message.edit_text('Нажали САМУЮ первую кнопку!', reply_markup=keyboard_inline)
    except:
        await callback.answer('УЖЕ нажали САМУЮ первую кнопку!')
