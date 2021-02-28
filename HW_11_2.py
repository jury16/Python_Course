"""
Create class Car. Attributes: brand, model, year of manufacture, speed (default 0).
Methods: increase speed (speed + 5), decrease speed (speed - 5), stop (reset speed to 0),
display speed, turn (change the sign of speed). All attributes are private.

"""


class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__year = year
        self.__model = model
        self.__speed = speed

    def increase_speed(self):
        self.__speed += 5
        print(self.__speed)

    def decrease_speed(self):
        self.__speed -= 5
        print(self.__speed)

    def stop(self):
        self.__speed = 0
        print(self.__speed)

    def display_speed(self):
        print(f'{self.__speed}')

    def reverse(self):
        self.__speed = -self.__speed
        return self.__speed


car = Car('BMW', '325', 1990, 65)
print(car._Car__brand)
car.increase_speed()