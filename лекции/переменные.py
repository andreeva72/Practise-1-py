
# - комментарий
#print() - вывод
#input() - запрос значения
#переменная - коробка, которая хранит в себе значение

name = "Катя" #строка - str()
age = 15 #целое число - int()
height = 5.4 #вещественные числа - float()
is_student = True #True/False - bool()

print("Hello word")
print("Привет"*5)
print("Сложение:", 5 + 3)            # Вывод: 8
print("Вычитание:", 5 - 3)           # Вывод: 2
print("Умножение:", 5 * 3)           # Вывод: 15
print("Деление:", 5 / 3)             # Вывод: 1.6666666666666667
print("Целочисленное деление:", 5 // 3) # Вывод: 1
print("Остаток от деления:", 5 % 3)   # Вывод: 2
print("Возведение в степень :", 5 ** 3) # Вывод: 125
print("Отрицание числа:", -5)          # Вывод: -5

box = 100
print(box)

"""
name = input("Как тебя зовут?")
print(name)
print(type(name))
"""
#type() - возвращает тип переменной
"""
age = int(input("Сколько тебе лет?"))
print(age)
print(type(age))
"""

#задачи
"""
a = int(input("Введите число"))
b = int(input("Введите число"))
sum = a + b
print(sum)

fahrenheit = float(input("Введите число"))
z = (fahrenheit - 32) * 5/9
print(z)

name = input("Введите имя:")
age = int(input("Введите возраст:"))

print(name, age)

"""

cal_apple = 4
cal_banana = 9
cal_bigmak = 560

eat_apple = int(input("Сколько ты съел яблок?"))
eat_banana = int(input("Сколько ты съел бананов?"))
eat_bigmak = int(input("Сколько ты съел бигмаков?"))

total = (cal_apple * eat_apple + cal_banana * eat_banana + cal_bigmak * eat_bigmak)

print(total, "ккал")

#3АДАЧИ
#1 Найти периметр и площадь прямоугольника
a = int(input("Введите 1 значение"))
b = int(input("Введите 2 значение"))
с = int(input("Введите "))
print("Периметр:", a+b+c)
print("Площадь:",  )
