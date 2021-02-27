#1.Make all attributes of the Dog class private.
# Make getter and setter for each attribute using decorators.
# Remove all change methods

class Dog:
    def __init__(self, height, weight, name, age, master):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age
        self.__master = master

    @property
    def height(self):
        return self.__height
    @property
    def weight(self):
        return self.__weight
    @height.setter
    def height(self, height):
        self.__height = height
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight = weight
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, master):
        self.__master = master

dog = Dog(95, 35, 'Sparky', 10, 'Yuri')

print(f"dog's master is: {dog.master}")
dog.master = 'Jon'
print(f"Now dog's master is: {dog.master}")
