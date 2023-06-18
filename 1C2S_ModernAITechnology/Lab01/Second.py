import numpy as np
from keras.datasets import mnist
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense

# Для решения задачи классификации рукописных цифр на примере базы MNIST можно использовать различные алгоритмы машинного обучения, такие как метод опорных векторов (SVM), случайный лес (Random Forest), нейронные сети и т.д. В данном примере мы будем использовать нейронную сеть с помощью библиотеки Keras.
# ---Загрузка данных
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# ---Подготовка данных
# Нормализация значений пикселей
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255
# Преобразование меток классов в формат one-hot encoding
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# ---Создание модели
# Создание последовательной модели
model = Sequential()
# Добавление первого слоя Dense с 512 нейронами и функцией активации relu
model.add(Dense(512, activation='relu', input_shape=(28 * 28,)))

# Добавление второго слоя Dense с 10 нейронами и функцией активации softmax
model.add(Dense(10, activation='softmax'))

#---Компиляция модели
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

#---Обучение модели
model.fit(train_images, train_labels, epochs=5, batch_size=128)


#---Оценка точности модели на тестовой выборке
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('Точность на тестовой выборке:', test_acc)


#---Предсказание меток классов для тестовой выборки
predictions = model.predict(test_images)