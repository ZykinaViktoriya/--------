# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, 
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

import random
lst = int(input('Введите длину массива: '))
one = [random.randint(-10, 10) for i in range(lst)]

# count = 0
# for i in range(1 , lst - 1):
#     if one[i - 1] < one[i] > one[i + 1]:
#         count += 1
# print(one)
# print(count)        

count = sum(one[i - 1] < one[i] > one[i + 1] for i in range(1, lst - 1))

print(one)
print(count)