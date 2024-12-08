

class Circle:


    def __init__(self: object, radius: int) -> None:

        self.__radius = radius


    def get_radius(self: object) -> int:

        return self.__radius


    def set_radius(self: object, radius: int) -> None:

        self.__radius = radius



circle = Circle(10)
circle1 = Circle(20)

print(circle.get_radius()) # Вывод будет 10

print(circle1.get_radius()) # Вывод будет 20

circle.set_radius(12) # Изменяет атрибут radius у экземпляра circle, radius был 10 станет 12

circle1.set_radius(32) # Изменяет атрибут radius у экземпляра circle1, radius был 20 станет 32

print(circle.get_radius()) # Вывод будет 12

print(circle1.get_radius()) # Вывод будет 32

