"""
Create parent class Pet, containing all common methods of Dog, Cat, Parrot classes.
# Inherit Dog, Cat, Parrot from the Pet class. Remove in child classes those methods
# that the parent class has. Create an object of each class and call all of its methods.
"""
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def run(self):
        return "I'm running!"
    def jump(self):
        return "I jump!"
    def sleep(self):
        return "I'm sleeping!"
    def birthday(self):
        return self.age + 1

class Dog(Pet):
    def bark(self):
        return 'Bark!'
class Cat(Pet):
    def meow(self):
        return 'Meow!'
class Parrot(Pet):
    def fly(self):
        return 'I fly'

dog = Dog('Sparky', 15)
cat = Cat('Ktty', 5)
parrot = Parrot('Kar', 35)

print(f'Dog do : {dog.run()}, {dog.jump()}, {dog.sleep()}, I say: {dog.bark()}, and today i am {dog.birthday()} years old')

print(f'Cat do : {cat.run()}, {cat.jump()}, {cat.sleep()}, I say: {cat.meow()}, and today i am {cat.birthday()} years old')

print(f'Parrot do : {parrot.run()}, {parrot.jump()}, {parrot.sleep()}, {parrot.fly()}, and today i am {parrot.birthday()} years old')


