# Create three classes: Dog, Cat, Parrot. Attributes of each class: name, age, master.
# Each class contains a constructor and methods: run, jump, birthday (increases age by 1), sleep.
# The Parrot class has an additional fly method. Cat - meow, Dog - bark.

class Dog:
    def __init__(self,height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def run(self):
        return "I'm running!"
    def jump(self):
        return "I jump!"
    def sleep(self):
        return "I'm sleeping!"
    def bark(self):
        return 'Bark!'
    def birthday(self, age):
        return age + 1

class Cat:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def run(self):
        return "I'm running!"
    def jump(self):
        return "I jump!"
    def sleep(self):
        return "I'm sleeping!"
    def meow(self):
        return 'Meow!'
    def birthday(self, age):
        return age + 1

class Parrot:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def run(self):
        return "I'm running!"
    def jump(self):
        return "I jump!"
    def sleep(self):
        return "I'm sleeping!"
    def birthday(self, age):
        return age + 1
    def fly(self):
        return "I'm flaying!"

