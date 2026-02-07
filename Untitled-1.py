"""
#Задача 1 (скидка)
from abc import ABC, abstractmethod
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @abstractmethod
    def dicount_price(self):
        pass

class Promo(Product):
    def dicount_price(self):
        return self.price * 0,8
class PromoX2(Product):
    def dicount_price(self):
        return self.price * 0,4

phone = [Promo('Iphone 15', 100000), PromoX2('Iphone 17', 150000)]
for ph in phone:
    print(ph.dicount_price())
"""
"""
#Задача 2
class Duck:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "кря-кря"
    def swim(self):
        return "утка плавает"
    
class Dog:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "гав-гав"
    def run(self):
        return "собака бегает"
    
class Fish:
    def __init__(self, name):
        self.name = name
    def swim(self):
        return "рыба плавает"
    
class Robot:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "бип-бип"
    def walk(self):
        return "робот гуляет"


def make_sound_animal(animal):
    if hasattr(animal, "make_sound"):
        return animal.make_sound()
    else:
        return("животное не издаёт звуков")

def swim_animal(animal):
    if hasattr(animal, "swim"):
        return animal.swim()
    else:
        return("животное не плавает")


animals = [Duck("дональд дак"), Dog("джаггер"), Fish("дори"), Robot("джек")]
for animal in animals:
    print(make_sound_animal(animal))
    
for animal in animals:
    print(swim_animal(animal))
"""

#Задача 3
from abc import ABC, abstractmethod
class Pay:
    def __init__(self, summa, sp_pay):
        self.summa = summa
        self.sp_pay = sp_pay
    @abstractmethod
    def price_pay(self):
        pass

class Nal_pas(Pay):
    def price_pay(self):
        return self.summa - (self.summa * 0.01)

class Pr_pas(Pay):
    def price_pay(self):
        return self.summa - (self.summa * 0.03)

sp = [Nal_pas(4000, "Наличные"), Pr_pas(4000, "Перевод")]

for i in sp:
    print(i.price_pay())