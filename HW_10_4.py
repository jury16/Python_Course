"""
Review your assignment, where you implemented the Car class (HW_12_1)
and think about where to add throwing (raise) exceptions (for example,
when the speed may become less than 0). Where you are working with this class,
add handling for these exceptions using the try construct.

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
        if self.__speed < 0:
            raise ValueError('Negative speed!')
        print(self.__speed)




    def stop(self):
        self.__speed = 0
        print(self.__speed)

    def display_speed(self):
        print(f'{self.__speed}')

    def reverse(self):
        self.__speed = -self.__speed
        return self.__speed
    
car = Car('BMW', '325', 1990, 3)
# print(car._Car__brand)
# car.increase_speed()

try:
    car.decrease_speed()
except ValueError as e:
    print(e)