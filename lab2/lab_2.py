"""
Предметная область: Введение в информационные технологии.

Лабораторная работа №2. Функции в Python и базовые алгоритмы

Цель работы: Освоить принципы определения и использования функций в языке программирования Python, 
    понять механизмы передачи аргументов в функции, научиться применять функции для решения практических задач, 
    а также изучить базовые алгоритмические конструкции

Группа: БВТ2402

Студент: Юдин Дмитрий Сергеевич

"""


import math

"""
Задание 1: Написание простых функций

    1) Напишите функцию greet, которая принимает имя пользователя в качестве аргумента и выводит 
    приветствие с этим именем.
    2)Создайте функцию square, которая возвращает квадрат переданного ей числа.
    3) Реализуйте функцию max_of_two, которая принимает два числа в качестве аргументов и возвращает большее из них.

"""

def great(name: str) -> None:
    print(f"Привет, {name}!")


def square(num: int) -> int:
    return math.pow(num, 2)


def max_of_two(num1: int, num2: int) -> int:
    return max(num1, num2)



"""
Задание 2: Работа с аргументами функций

    4) Напишите функцию describe_person, принимающую имя и возраст человека, и печатающую эту информацию в читаемом виде. 
Сделайте возраст опциональным аргументом со значением по умолчанию 30.

"""

def describe_person(name: str, age: int=30) -> None:
    print(f"Привет, вас зовут: {name}. Ваш возраст: {age}.")



"""
Задание 3: Использование функций для решения алгоритмических задач

    5) Напишите функцию is_prime, которая определяет, является ли число простым, 
    и возвращает True или False соответственно.

"""

def is_prime(num: int) -> bool:

    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  
    
    return True

while True: 
    great(input("1) Введтие свое имя: "))

    square(int(input("2) Введите число для возведения в квадрат: ")))

    print("3) Найти большее число")

    max_of_two(int(input("1) Введите первое число: ")), int(input("Введите второе число: ")))
    
    describe_person(input("Введите ваше имя: "), int(input("Введите ваш возраст: ")))

    is_prime(int(input("Введтие число: ")))