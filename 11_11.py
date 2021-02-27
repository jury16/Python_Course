"""
Add two new attributes to the parent class: weight and height.
Add change_weight, change_height methods that take one parameter and add it to the corresponding argument.
If the parameter was not passed, increase by 0.2. Modify the fly method of the Parrot class.
If the weight is more than 0.1, display the message This parrot cannot fly.

"""
class Pet:
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
    def birthday(self):
        return self.age + 1
    def change_weight(self, weight = 0.2):
        self.weight = self.weight + weight
        return self.weight
    def change_height(self, height = 0.2):
        self.height = self.height + height
        return self.height

class Dog(Pet):
    def bark(self):
        return 'Bark!'
class Cat(Pet):
    def meow(self):
        return 'Meow!'
class Parrot(Pet):
    def fly(self):
        if self.weight > 0.1:
            return "This parrot can't fly!"
        return 'I fly'

dog = Dog(95, 35, 'Sparky', 10)
cat = Cat(25, 15, 'Kitty', 2)
parrot = Parrot(15, 3, 'Kar', 100)
print(f'Dog name is : {dog.name}, height is: {dog.height} cm, weight is {dog.weight} kf, age is {dog.age} years')
print(f'Dog do : {dog.run()}, {dog.jump()}, {dog.sleep()}, I say: {dog.bark()}, and today i am {dog.birthday()} years old')
print(f'Cat name is : {cat.name}, height is: {cat.height} cm, weight is {cat.weight} kf, age is {cat.age} years')
print(f'Cat do : {cat.run()}, {cat.jump()}, {cat.sleep()}, I say: {cat.meow()}, and today i am {cat.birthday()} years old')
print(f'Parrot name is : {parrot.name}, height is: {parrot.height} cm, weight is {parrot.weight} kf, age is {parrot.age} years')
print(f'Parrot do : {parrot.run()}, {parrot.jump()}, {parrot.sleep()}, {parrot.fly()}, and today i am {parrot.birthday()} years old')
print(dog.change_weight())
print(parrot.fly())

