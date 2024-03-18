import asyncio
import logging
from aiogram import Bot, Dispatcher
from Config_data.config import Config, load_config
from Handlers import other_handlers

# from Param.const import pathes
# from Param import const


# print(class_labels)

# Инициализируем логер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main() -> None:
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
        '[%(asctime)s] - %(name)s  - %(message)s'
    )
    # Выводим в консоль информацию о начале запуска
    logger.info('Starting InteriorClass')                   # У него Lesson

    # Загружаем конфиг в переменную config
    config: Config = load_config()
    # config: Config = load_config(".env")

    # Инициализируем бота и диспетчера
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(other_handlers.router)


    # Пропускаем накопившиеся апдейты (сообщения) и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    # bot.polling(none_stop=True) # Что-то такое нужно?

if __name__ == "__main__":
    asyncio.run(main())

























# # РАБОЧИЙ ВАРИАНТ
# # cv2 устанавливается как opencv-python
# # pip install keras_preprocessing
#
# import asyncio
# import logging
# import sys
# from os import getenv
#
# from aiogram import Bot, Dispatcher, Router, types, F
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.types import Message
# from aiogram.utils.markdown import hbold
#
# from PIL import Image
# from keras.preprocessing.image import load_img
#
# # from aiogram.dispatcher import filters
# # from app.loader import dp
#
# # Import necessary libraries for image recognition
# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
#
# # Load the pre-trained image recognition model
# model = keras.models.load_model('C:\POD\TMP\classes_33_predikt_0_9136363863945007.h5')
#
# # Bot token can be obtained via https://t.me/BotFather
# # TOKEN = getenv("BOT_TOKEN")
# TOKEN = '6388006569:AAF4cKig5E1hTAH7O0mVqkFC1unedTGLbU0'
#
# # All handlers should be attached to the Router (or Dispatcher)
# dp = Dispatcher()
#
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     # Most event objects have aliases for API methods that can be called in events' context
#     # For example if you want to answer to incoming message you can use `message.answer(...)` alias
#     # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
#     # method automatically or call API method directly via
#     # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
#     # await message.answer(f"Hello, {hbold(message.from_user.full_name)}! Отправь мне фотографию, и я попробую ее классифицировать.")
#     await message.answer(f"Hello, {hbold(message.from_user.full_name)}! Send me a photo and I'll try to classify it.")
#
# @dp.message(F.text)  # Handle photo messages
# async def any_text_handler(message: types.Message, bot: Bot):
#     # await message.answer(f"The image is recognized as: {label}")
#     # await message.answer(f"Hello, {hbold(message.from_user.full_name)}! Отправь мне фотографию, и я попробую ее классифицировать.")
#     await message.answer(f"Hello, {hbold(message.from_user.full_name)}! Send me a photo and I'll try to classify it.")
#
# @dp.message(F.photo)  # Handle photo messages
# async def download_photo(message: types.Message, bot: Bot):
#
# # Download the photo
# #     print("1111111")
#     await bot.download(
#         message.photo[-1],
#         destination=f"/tmp/{message.photo[-1].file_id}.jpg"
#     )
#     # photo = await message.photo[-1].download()
#     # print('OK')
#
#     # Пример использования load_img
#     # img = load_img('image.jpg', target_size=(224, 224))
#     # img = load_img(f"/tmp/{message.photo[-1].file_id}.jpg", target_size=(224, 224))# Так работает
#
#     # Perform image recognition
#     # image = keras.preprocessing.image.load_img(photo, target_size=(224, 224))
#     image = keras.preprocessing.image.load_img(f"/tmp/{message.photo[-1].file_id}.jpg", target_size=(224, 224))
#     image_array = keras.preprocessing.image.img_to_array(image)
#     # print('image_array.shape=', image_array.shape)
#     # image_array = image_array / 255.0  # Нормализация значений пикселей - ни в коем случае, с ним не распознается!!!
#     # print('image_array.shape=', image_array.shape)
#
#     image = tf.expand_dims(image_array, axis=0)
#     # Классификация изображения
#     predictions = model.predict(image)
#
#
#     # Примените функцию softmax для получения вероятностей
#     probabilities = tf.nn.softmax(predictions).numpy()[0]
#
#     # print('predictions=', predictions)
#     print('probabilities=', probabilities)
#
#     # Получите индекс класса с наивысшей вероятностью
#     predicted_class_index = tf.argmax(probabilities).numpy()
#
#     # Получите название класса
#     # class_labels = ["класс1", "класс2", "класс3"]  # Замените на свои метки классов
#     class_labels = \
# ['Electrical Works - Ceiling fan',
#  'Electrical Works - Electrical panel',
#  'Electrical Works - Lamp',
#  'Electrical Works - Light fixture',
#  'Electrical Works - Socket',
#  'Electrical Works - Switch',
#  'Electrical Works - Wiring',
#  'Flooring - Carpet',
#  'Flooring - Linoleum',
#  'Flooring - Liquid screed',
#  'Flooring - Vinyl flooring',
#  'Painting - Ceiling',
#  'Painting - Decorative painting',
#  'Painting - Decorative plaster',
#  'Painting - Door',
#  'Painting - Molding',
#  'Painting - Wall',
#  'Painting - Wallpaper',
#  'Painting - Window',
#  'Painting - Window trim',
#  'Plumbing Works - - Water heater',
#  'Plumbing Works - Bathtub',
#  'Plumbing Works - Drainage system',
#  'Plumbing Works - Faucet',
#  'Plumbing Works - Pipes',
#  'Plumbing Works - Shower cabin',
#  'Plumbing Works - Sink',
#  'Plumbing Works - Siphon',
#  'Plumbing Works - Tap',
#  'Plumbing Works - Toilet',
#  'Tiling - Kitchen backsplash tile',
#  'Tiling - Mosaic',
#  'Tiling - Tile']
#     predicted_class_label = class_labels[predicted_class_index]
#
#     # Получите вероятность для предсказанного класса
#     predicted_probability = probabilities[predicted_class_index]
#
#     # ptr=tf.argmax(predictions, axis=1)
#     # confidence = np.max(predictions[ptr])
#
#     # label = 'Класс изображения: ' + str(tf.argmax(predictions, axis=1).numpy()[0])
#     # label = 'Класс изображения: ' + str(ptr) + ' с вероятностью ' + str(confidence)
#
#     # label= f'{predicted_class_label} с вероятностью {predicted_probability*100:.0f}%.'
#     label= f'"{predicted_class_label}" with probability {predicted_probability*100:.0f}%.'
#     # await message.answer(f"The image is recognized as: {predicted_class}")
#     await message.answer(f'The image is recognized as: {label}')
#
# async def main() -> None:
#     # Initialize Bot instance with a default parse mode which will be passed to all API calls
#     bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
#     # And the run events dispatching
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
