import numpy as np

# 1. Создайте единичную матрицу 3*3
I = np.eye(3)
print(I)

# 2. Создайте матрицу 5*5 со значениями 1, 2, 3, 4 ниже диагонали
# 1 вариант (как левая треугольная матрицаб где в первом столбце 1-4, во втором 1-3 и тд)
n = 5
i, j = np.indices((n, n))
M = np.where(i > j, i - j, 0)
print(M)

# 2 вариант (если просто в нижней поддиагонали 1,2,3,4)
n = 5
M = np.zeros((n, n))
for i in range(1, n):
    M[i, :i] = i
print(M)

# 3. Что будет получено в результате выполнения данного кода?
# print(sum(range(5), -1)) # 9
# from numpy import *
# print(sum(range(5), -1)) # 10

# 4 Как найти самое часто встречающееся значение среди элементов двух массивов?
arr1 = np.array([1, 2, 2, 2, 2, 3, 7])
arr2 = np.array([ 3, 4, 5])
common_elements = np.intersect1d(arr1, arr2)
combined = np.concatenate((arr1, arr2))
values, counts = np.unique(combined, return_counts=True)
mask = np.isin(values, common_elements)
filt_values = values[mask]
filt_counts = counts[mask]
most_frequent_common = filt_values[np.argmax(filt_counts)]
print(most_frequent_common)

# Как игнорировать варнинги
# import warnings
# warnings.filterwarnings('ignore')


# 6 Реализуем функцию генератор, которая генерирует 10 целых чисел
def generate_integers():
    for i in range(10):
        yield i * 2

arr = np.fromiter(generate_integers(), dtype=int, count=10)
print(arr)

# 7. Создать массив случайных чисел размеорм 10 и отсортировать
arr = np.random.randint(0, 100, size=10)
arr_sorted = np.sort(arr)

print("Исходный массив:", arr)
print("Отсортированный:", arr_sorted)

# 8. Создайте случайную матрицу 10x2 которая представляет собой декартовые координаты и преобразуйте их в полярные
cartesian = np.random.uniform(-10, 10, size=(10, 2))

x = cartesian[:, 0]
y = cartesian[:, 1]

r = np.sqrt(x**2 + y**2)
phi = np.arctan2(y, x)
polar = np.column_stack((r, phi))

print("Декартовы координаты (X, Y):\n", cartesian)
print("\nПолярные координаты (r, phi):\n", polar)


# 9. Создайте структурированный массив который будет описывать пиксель(координату x, y и цвет r,g,b)
pixel_dtype = [
    ('x', 'i4'),
    ('y', 'i4'),
    ('r', 'u1'),
    ('g', 'u1'),
    ('b', 'u1')
]

pixels = np.zeros(2, dtype=pixel_dtype)

pixels['x'] = [10, 20]
pixels['y'] = [5, 15]
pixels['r'] = [255, 0]
pixels['g'] = [0, 255]
pixels['b'] = [0, 0]

print(pixels)
print("\nКоординаты X:", pixels['x'])
print("\nПервый пиксель:", pixels[0])

# 10. Как конвертировать тип массив от float32 в int32 in place?
arr = np.array([1.5, 2.7, 3.1], dtype=np.float32)
print("До:", arr.dtype)  # float32

arr = arr.astype(np.int32, copy=False)
print("После:", arr.dtype)
print("Значения:", arr)