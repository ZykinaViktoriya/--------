# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

lst = [1, 2, 3, 4, 5]
print(lst)
k = int(input())
for i in range(k):
    lst.insert(0,lst.pop())
print(lst)

# lst = [1, 2, 3, 4, 5]
# print(lst)
# k = int(input())
# print(lst[-k:] + lst[:-k])