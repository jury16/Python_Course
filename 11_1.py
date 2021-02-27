#Create an empty class Dog
#Create two Dog objects. Display them on the screen
#Add two methods to the Dog class: jump and run. Methods display Jump! and Run!



class Dog:
    def jump(self):
        return 'Jump'
    def run(self):
        return 'Run'


dog1 = Dog()
dog2 = Dog()
print(f'Dog_1: {dog1}, Dog_2: {dog2}')
print(f'dog2 run: {dog2.run()}')
print(f'dog1 jump: {dog1.jump()}')
