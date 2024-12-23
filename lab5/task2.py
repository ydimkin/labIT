class Circle:


    def __init__(self: object, radius: int) -> None:

        self.__radius = radius


    def get_radius(self: object) -> int:

        return self.__radius


    def set_radius(self: object, radius: int) -> None:

        self.__radius = radius



circle = Circle(10)

print(circle.get_radius()) 

circle.set_radius(12) 

print(circle.get_radius())
 

