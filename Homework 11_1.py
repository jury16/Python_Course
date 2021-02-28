"""
Create five classes describing real objects. Each
class must contain at least three private attributes, a constructor,
getters and setters for each attribute, two methods.

"""
class CdPlayer:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def play_music(self):
        print('play music')
    def play_radio(self):
        print('play radio')

    def get_brand(self):
        print(self.brand)
    def set_brand(self, brand):
        self.brand = brand


class DvdPlayer:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color

    def play_music(self):
        print('play music')

    def play_video(self):
        print('play video')
    def play_radio(self):
        print('play radio')

    def get_brand(self):
        print(self.brand)
    def set_master(self, brand):
        self.brand = brand
    def get_color(self):
        print(self.brand)
    def set_color(self, brand):
        self.brand = brand

class Fridge:
    def __init__(self, brand, year, color, temperature):
        self.brand = brand
        self.year = year
        self.color = color
        self.temperature = temperature

    def freeze(self):
        print('freeze goods')

    def cool(self):
        print('cool goods')

    def get_temperature(self):
        self.temperature
        print(enumerate)

    def set_temperature(self, temperature):
        self.temperature = temperature

class Microwave:
    def __init__(self, brand, year, color, power):
        self.brand = brand
        self.year = year
        self.color = color
        self.power = power

    def warm(self):
        print('warm up goods')

    def get_power(self):
        self.power

    def set_power(self, power):
        self.power = power


class AlarmClock :
    def __init__(self, brand, year, color, radio=0):
        self.brand = brand
        self.year = year
        self.color = color
        self.radio = radio

    def alarm(self):
        print('alarm!!!')
    def play_radio(self):
        print('play radio')

    def get_brand(self):
        return self.brand

    def set_power(self, brand):
        self.brand = brand
