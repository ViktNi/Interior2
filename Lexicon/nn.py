# Import necessary libraries for image recognition
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
from keras.preprocessing.image import load_img


from Param.class_labels_en import class_labels
from Param import const

def get_predicts(file_path):
    # Load the pre-trained image recognition model
    model = keras.models.load_model(const.pathes['model_path'])

    # image = keras.preprocessing.image.load_img(f"/tmp/{message.photo[-1].file_id}.jpg", target_size=(224, 224))
    image = keras.preprocessing.image.load_img(file_path, target_size=(224, 224))
    image_array = keras.preprocessing.image.img_to_array(image)
#     # image_array = image_array / 255.0  # Нормализация значений пикселей - ни в коем случае, с ним не распознается!!!
    image = tf.expand_dims(image_array, axis=0)
    # Классификация изображения
    predictions = model.predict(image)

    # Применим функцию softmax для получения вероятностей
    probabilities = tf.nn.softmax(predictions).numpy()[0]

    # print('predictions=', predictions)
    print('probabilities=', probabilities)

    # # Получите индекс класса с наивысшей вероятностью
    # predicted_class_index = tf.argmax(probabilities).numpy()

    # Найдем индексы трех максимальных значений, сами эти значения и соответствующие им метки классов
    max_indices = sorted(range(len(probabilities)), key=lambda i: probabilities[i], reverse=True)[:3]
    max_probabilities = [probabilities[i] for i in max_indices]
    predicted_class_labels = [class_labels[i] for i in max_indices]

    print(f'max_indices={max_indices}')

    # predicted_class_label = class_labels[predicted_class_index]
    #
    # # Получите вероятность для предсказанного класса
    # predicted_probability = probabilities[predicted_class_index]

    # ptr=tf.argmax(predictions, axis=1)
    # confidence = np.max(predictions[ptr])

    # # label = 'Класс изображения: ' + str(tf.argmax(predictions, axis=1).numpy()[0])
    # # label = 'Класс изображения: ' + str(ptr) + ' с вероятностью ' + str(confidence)
    # # label= f'{predicted_class_label} с вероятностью {predicted_probability*100:.0f}%.'
    # label = f'The image is recognized as: "{predicted_class_label}" with probability {predicted_probability * 100:.0f}%.'
    # # await message.answer(f"The image is recognized as: {predicted_class}")

    # return label
    return predicted_class_labels, max_probabilities










