import numpy as np
from scipy import spatial

num_points = 2000 # количество вершин
points_coordinate = np.random.rand(num_points, 2)  # генерация рандомных вершин
print("Координаты вершин:\n", points_coordinate[:10], "\n")

# вычисление матрицы расстояний между вершин
distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
print("Матрица расстояний:\n", distance_matrix)