"""
class BankAccount:
    def _init_(self, account_number, account_owner, balance):
        self.__account_number = account_number 
        self._account_owner = account_owner 
        self.__balance = balance
    def get_account_number(self):
        return self.__account_number
    def get_account_owner(self):
        return self.__account_owner
    def get_balance(self):
        return self.__balance

    def deposit(self):
        if amount > 0:
            self.__balance+=amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance-=amount
            return True
        return True
    def info(self):
        print(self.__account_number)
        print(self.__account_owner)
        print(self.__balance)

bank1 = BankAccount (1234134, "Иван Петров", 1000)

bank1.get__account_number()
bank1.get__account_owner()
bank1.get__balance()

bank1.deposit(500)
bank1.withdraw(300)
bank1.info()
"""

"""
Создайте класс Student:
1. Приватные атрибуты: _name, _grades (список оценок)
2. Методы: add_grade(grade), get_average(), get_name()
3. Оценки можно только добавлять, нельзя удалять или менять напрямую
"""
class Student:
    def __init__(self, name):
        self.__name = name
        self.grades = []
    def get_name(self):
        return self.name
    def get_grades(self):
        return self.__grades
    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 1 <= grade <= 5:
            self.__grades.append(grade)
            return True
        return False
    def get_average(self):
        if not self.__grades:
            return 0
        return sum(self.__grades)/len(self.__grades)
    def info(self):
        print(self.__grades)
        print(self.__name)
        print(self.get_average())

student1 = Student("Чередниченко Юрий")
student2 = Student("Власова Милана")

student1.add_grade(5)
student1.add_grade(4)
student2.add_grade(3)
student2.add_grade(5)

student1.info()
student2.info()


# # Создайте класс Car, который представляет автомобиль с полной защитой данных через механизмы инкапсуляции.

# Требования к классу:

# 1. Приватные атрибуты:
#    - _model (строка) - модель автомобиля
#    - _year (целое число) - год выпуска
#    - _mileage (целое число) - пробег в километрах
#    - _fuel_level (вещественное число) - уровень топлива в литрах

# 2. Публичные методы:
#    - drive(km) - проехать заданное расстояние в км
#      * Проверяет, достаточно ли топлива для поездки
#      * Расход топлива: 10 литров на 100 км (0.1 л/км)
#      * Если топлива достаточно, увеличивает пробег и уменьшает уровень топлива
#      * Возвращает строку с результатом операции

#    - refuel(liters) - заправить автомобиль
#      * Проверяет, что количество литров положительное
#      * Увеличивает уровень топлива
#      * Возвращает строку с результатом операции

#    - get_info() - получить информацию об автомобиле
#      * Возвращает форматированную строку с моделью, годом, пробегом и уровнем топлива
#     #

class Car:
    def __init__(self, model, year, mileage, fuel_level):
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__fuel_level = fuel_level

    def get__model():
        return self.__model
    def get__year():
        return self.__year
    def get__mileage():
        return self.__mileage
    def get__fuel_level():
        return self.__fuel_level

    def drive(self, km):
        if km > 0 and self.__fuel_level >= km*0.1:
            self.__mileage += km
            self.__fuel_level -= km-0.1
            return km

    def refuel(self, ):
        if litr > 0:
            self.__fuel_level += litr
            return litr
    def info(self):
        return self.__model, self.__year, self.__mileage, self.__fuel_level

car = Car("мпрло", 2005)
