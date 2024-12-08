import random
from math import sqrt
from datetime import date
from my_module import adder
from my_lib import *


#Задание №1
fun = lambda x: sqrt(x)

print(fun(int(input("Введите число для вычисления корня: "))))

print(f"Дата сегодня: {date.today()}")

#Задание №2 
print(f"Сумма чисел: {adder(20, 40)}")


#Задание №3
spiral_matrix(random.randint(4, 10))

triangle(random.randint(4, 10))

arr = [random.randint(1, 999) for i in range(25)]

print(*arr)

arr = quicksort(arr)

print(*arr)

digit = random.choice(arr)

print(digit)

print(binary_search(arr, digit))





