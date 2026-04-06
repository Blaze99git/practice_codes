'''
1. Basic Class and Object
Problem: Create a Car class with attributes like brand and model. 
Then create an instance of this class.

2. Class Method and Self
Problem: Add a method to the Car class that displays the full name of the car (brand and model).

3. Inheritanc
Problem: Create an ElectricCar class that inherits from the Car class and has an additional 
attribute battery_size.

4. Encapsulation
Problem: Modify the Car class to encapsulate the brand attribute, making it private, 
and provide a getter method for it.

5. Polymorphism
Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and 
ElectricCar classes, but with different behaviors.

6. Class Variables
Problem: Add a class variable to Car that keeps track of the number of cars created.

7. Static Method
Problem: Add a static method to the Car class that returns a general description of a car.

8. Property Decorators
Problem: Use a property decorator in the Car class to make the model attribute read-only.

9. Class Inheritance and isinstance() Function
Problem: Demonstrate the use of isinstance() to check if my_tesla is an 
instance of Car and ElectricCar.

10. Multiple Inheritance
Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from 
both, demonstrating multiple inheritance.
'''
# 1. Basic Class and Object
class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Encapsulated attribute
        self._model = model   # Protected attribute

    # 2. Class Method and Self
    def display_full_name(self):
        return f"{self.__brand} {self._model}"

    # 4. Encapsulation - Getter for brand
    def get_brand(self):
        return self.__brand

    # 5. Polymorphism
    def fuel_type(self):
        return "Gasoline"

    # 6. Class Variables
    car_count = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self._model = model
        Car.car_count += 1

    # 7. Static Method
    @staticmethod
    def general_description():
        return "A car is a road vehicle, typically with four wheels, powered by an internal combustion engine."

    # 8. Property Decorators
    @property
    def model(self):
        return self._model
# 3. Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    # 5. Polymorphism
    def fuel_type(self):
        return "Electricity"
# 10. Multiple Inheritance
class Battery:
    def battery_info(self):
        return "This is a battery."
class Engine:
    def engine_info(self):
        return "This is an engine."
class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        Car.__init__(self, brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electricity"
# Demonstration
my_tesla = ElectricCar("Tesla", "Model S", "100 kWh")
print(my_tesla.display_full_name())  # Tesla Model S
print(my_tesla.get_brand())           # Tesla
print(my_tesla.fuel_type())           # Electricity
print(Car.general_description())      # A car is a road vehicle...
print(f"Total cars created: {Car.car_count}")  # Total cars created:
print(isinstance(my_tesla, Car))         # True
print(isinstance(my_tesla, ElectricCar)) # True
print(my_tesla.battery_info())          # This is a battery.
print(my_tesla.engine_info())           # This is an engine.
print(my_tesla.model)                   # Model S
# my_tesla.model = "Model X"  # This will raise an AttributeError
# because model is read-only due to the property decorator.
def __init__(self, brand, model):
    self.__brand = brand  # Encapsulated attribute
    self._model = model   # Protected attribute
    Car.car_count += 1