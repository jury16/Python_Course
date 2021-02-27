# 1.Create an empty class Dog
# 2.Create two Dog objects. Display them on the screen
# 3.Add two methods to the Dog class: jump and run. Methods display Jump! and Run!
# 4.Add the change_name method to the Dog class.
# The method accepts a new name as input and changes the name attribute of the object.
# Create one class object. Display name. Call the change_name method. Display name.


class Dog:
    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        return 'JUMP!'

    def run(self):
        return 'RUN!'

    def bark(self):
        return 'WOW!'
    def change_name(self, name):
        self.name = name

dog = Dog(95, 35, 'Sparky', 10)
print(dog.height, dog.weight, dog.name, dog.age)
print(dog.jump())
print(dog.run())
print(dog.bark())
print(f"dog's name is: {dog.name}")
dog.change_name('Rocky')
print(f"dog's name now is: {dog.name}")
