#1.Add a new private attribute to the initialization method - master.
#Create a get_master () method that returns the value of the master attribute.
#2.Add a new private attribute address (by default it is ‘Minsk’).
# Add getter and setter for address.
class Dog:
    def __init__(self, height, weight, name, age, master, address='Minsk'):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age
        self.__master = master
        self.__address = address

    def get_master(self):
        return self.__master
    def set_master(self, master):
        self.__master = master

    def get_address(self):
        return self.__address
    def set_address(self, address):
        self.__address = address


dog = Dog(95, 35, 'Sparky', 10, 'Yuri')

print(f"dog's master is: {dog.get_master()}")
dog.set_master('Jon')
print(f"Now dog's master is: {dog.get_master()}")
print(f"dog's address is: {dog.get_address()}")
dog.set_address('Bobruisk')
print(f"dog's address is: {dog.get_address()}")
