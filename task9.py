# Задача 9. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# 5->120

# n = int(input('Введите число n:\n'))
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
 
# print(factorial)5

n = int(input('Введите число n:\n'))
factorial = 1
 
for i in range(1, n+1):
    factorial *= i
 
print(factorial)