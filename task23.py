# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

import random

lst = [random.randint(0, 10) for i in range(10)]
print(lst)
count = 0
for i in range(1, len(lst)):
    if lst[i] > lst[i-1]:
        count += 1
print(count)        