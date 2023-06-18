

def ackley(x):
    """Функция Экли"""
    d = len(x)
    a = 20
    b = 0.2
    c = 2 * np.pi
    sum1 = np.sum(x ** 2)
    sum2 = np.sum(np.cos(c * x))
    term1 = -a * np.exp(-b * np.sqrt(1 / d * sum1))
    term2 = -np.exp(1 / d * sum2)
    return term1 + term2 + a + np.exp(1)

def ant_colony_optimization(ackley, num_ants, num_iterations, alpha, beta, rho, q):
    """Муравьиный алгоритм"""
    num_dimensions = 2  # Количество измерений
    tau = np.ones((num_dimensions, num_dimensions))  # Феромонная матрица

    best_solution = None
    best_fitness = float('inf')

    for i in range(num_iterations):
        solutions = np.zeros((num_ants, num_dimensions))
        fitnesses = np.zeros(num_ants)

        for j in range(num_ants):
            current = np.random.randint(num_dimensions)  # Случайный выбор стартовой точки
            visited = [current]
            for k in range(num_dimensions - 1):
                # Выбор следующей точки с помощью правила выбора муравья
                probs = np.zeros(num_dimensions)
                unvisited = list(set(range(num_dimensions)) - set(visited))
                for l in unvisited:
                    probs[l] = tau[current][l]**alpha * (1.0 / ackley(np.array([current, l]))**beta)
                probs = probs / sum(probs)
                next = np.random.choice(range(num_dimensions), p=probs)
                visited.append(next)
                current = next
            solutions[j] = visited
            fitnesses[j] = ackley(visited)
            if fitnesses[j] < best_fitness:
                best_solution = visited
                best_fitness = fitnesses[j]

        # Обновление феромонной матрицы с помощью правила обновления феромона
        delta_tau = np.zeros((num_dimensions, num_dimensions))
        for j in range(num_ants):
            for k in range(num_dimensions - 1):
                delta_tau[int(solutions[j][k])][int(solutions[j][k+1])] += q / fitnesses[j]
        tau = (1 - rho) * tau + delta_tau

    return best_solution, best_fitness

# Запуск муравьиный алгоритма для функции Экли
num_ants = 50 # Количество муравьев
num_iterations = 500 # Количество итераций
alpha = 1 # Вес феромона
beta = 1 # Вес расстояния
rho = 0.5 # Коэффициент испарения феромона
q = 100 # Количество феромона, оставляемое муравьем на пути

best_solution, best_fitness = ant_colony_optimization(ackley, num_ants, num_iterations, alpha, beta, rho, q)

print(f"Лучшее решение: {best_solution}")
print(f"Лучшее значение функции: {best_fitness}")

# Визуализация функции и найденного решения
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        Z[i][j] = ackley([X[i][j], Y[i][j]])

ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.5)
ax.scatter(best_solution[0], best_solution[1], best_fitness, color='red', s=100)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

plt.show()

