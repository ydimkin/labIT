class Vehicle:

    fuel: int 

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def get_info(self):
        return self.make + ' ' + self.mode

class Car(Vehicle):

    def __init__(self: object, make: str, model: str, fuel_type: str):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        return f"{self.make}, {self.model}, {self.fuel_type}"

car = Car('BMW', 'm4', '100')

print(car.get_info())
