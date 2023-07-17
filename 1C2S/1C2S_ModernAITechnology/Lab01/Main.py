import numpy as np
from keras.datasets import mnist

def gradient(f, x, h=0.0001):
    """
    Вычисляет градиент функции f в точке x при помощи численного дифференцирования

    Параметры:
        f: функция, градиент которой требуется вычислить
        x: точка, в которой требуется вычислить градиент
        h: шаг дифференцирования, по умолчанию 0.0001

    Возвращает:
        Градиент функции f в точке x
    """
    grad = np.zeros_like(x)
    for i in range(len(x)):
        # Создаем вектор с шагом h вдоль оси i
        delta = np.zeros_like(x)
        delta[i] = h
        # Вычисляем приращение функции при заданном шаге
        f_plus = f(x + delta)
        f_minus = f(x - delta)
        delta_f = f_plus - f_minus
        # Вычисляем частную производную по i-ой оси
        grad[i] = delta_f / (2*h)
    return grad


def sigmoid(x):
 """
    Вычисляет градиент функции f в точке x при помощи численного дифференцирования

    Параметры:
        f: функция, градиент которой требуется вычислить
        x: точка, в которой требуется вычислить градиент
        h: шаг дифференцирования, по умолчанию 0.0001

    Возвращает:
        Градиент функции f в точке x
    """
 return 1/(1 + np.exp(-x))




def softmax(x):
    exp_x = np.exp(x)
    sum_exp_x = np.sum(exp_x, axis=1, keepdims=True)
    return exp_x / sum_exp_x

# Forward pass
def forward(x, w, b):
    z = np.dot(w, x) + b
    y = sigmoid(z)
    return y

def one_hot(labels, num_classes):
    """
    Функция для преобразования массива меток классов в массив one-hot векторов.
    
    Аргументы:
    labels -- массив целых чисел, метки классов
    num_classes -- количество классов
    
    Возвращает:
    one_hot -- массив one-hot векторов
    """
    one_hot = np.zeros((len(labels), num_classes))
    for i in range(len(labels)):
        one_hot[i, labels[i]] = 1
    return one_hot

# Backward pass
def backward(x, y, t):
    # Шаг 1: Вычисляем градиент функции ошибки по выходу сети:
    dEdy = y - t
    dydz = y * (1 - y)
    dzdw = x
    dEdw = dEdy * dydz * dzdw
    dEdb = dEdy * dydz
    return dEdw, dEdb

# Gradient descent
def gradient_descent(x, t, w, b, learning_rate):
    y = forward(x, w, b)
    dEdw, dEdb = backward(x, y, t)
    w_new = w - learning_rate * dEdw
    b_new = b - learning_rate * dEdb
    return w_new, b_new

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Reshape and normalize data
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# Define neural network architecture
input_size = 784
hidden_size = 128
output_size = 10
w1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros(hidden_size)
w2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros(output_size)

# Define training parameters
learning_rate = 0.1
num_epochs = 10
batch_size = 128
num_batches = x_train.shape[0] // batch_size

# Train neural network using batch gradient descent
for epoch in range(num_epochs):
    for batch in range(num_batches):
        # Select batch of data
        start = batch * batch_size
        end = start + batch_size
        x_batch = x_train[start:end]
        y_batch = y_train[start:end]
        
        # Forward pass
        z1 = np.dot(x_batch, w1) + b1
        y1 = sigmoid(z1)
        z2 = np.dot(y1, w2) + b2
        y2 = softmax(z2)
        
        # Backward pass
        dEdy2 = y2 - one_hot(y_batch, output_size)
        dy2dz2 = y2 * (1 - y2)
        dz2dw2 = y1
        dEdw2 = np.dot(dz2dw2.T, dEdy2 * dy2dz2)
        dEdb2 = np.sum(dEdy2 * dy2dz2, axis=0)
        dEdy1 = np.dot(dEdy2 * dy2dz2, w2.T)
        dy1dz1 = y1 * (1 - y1)
        dz1dw1 = x_batch
        dEdw1 = np.dot(dz1dw1.T, dEdy1 * dy1dz1)
        dEdb1 = np.sum(dEdy1 * dy1dz1, axis=0)
        
        # Update weights and biases
        w2 -= learning_rate * dEdw2
        b2 -= learning_rate * dEdb2
        w1 -= learning_rate * dEdw1
        b1 -= learning_rate * dEdb1
        
    # Evaluate model on test data
    y_pred = np.argmax(forward(x_test, w1, b1, w2, b2), axis=1)
    accuracy = np.mean(y_pred == y_test)
    print('Epoch {}/{}: Test accuracy = {:.3f}'.format(epoch+1, num_epochs, accuracy))