# Задача11. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# 5->6

n = int(input())
s = 0
s1 = 1
s2 = 1
while s1 < n or s2 < n:
    s1 = s1 + s2
    s2 = s1 + s2
    s += 2
if s1 == n:
        s = s + 1
if n + s1 == s2 or n + s2 == s1 or s1 == n:
    print(s)
else:
    print(-1)
