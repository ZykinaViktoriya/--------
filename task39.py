# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

import random

n = int(input('Введите число: '))
one = [random.randint(-10, 10) for i in range(n)]

m = int(input('Введите число: '))
two = [random.randint(-10, 10) for i in range(n)]

print(f'{one = }')
print(f'{two = }')

result = (el for el in one if el not in two)
print(*result)