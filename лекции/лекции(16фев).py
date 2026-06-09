import pickle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(4, 5)

with open("main1.pkl", "wb") as file:
    pickle.dump(point, file)

with open("main1.pkl", "rb") as file:
    loaded_x_y = pickle.load(file)

print(f"Загруженная точка: x={loaded_x_y.x}, y={loaded_x_y.y}")

with open("main1.pkl", "rb") as file:
    raw = file.read(50)
    print(f"Сырые данные (первые 50 байт): {raw}")

import pickle

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [Point(4, 5), Point(6, 7), Point(9, 0)]

with open("main1.pkl", "wb") as file:
    pickle.dump(points, file)

with open("main1.pkl", "rb") as file:
    loaded_x_y = pickle.load(file)

for i in loaded_x_y:
    print(i.x, i.y)



import json

#ПРИМЕР 1: Работа с простым словарем
student = {
    "Anna": 34,
    "Anna1": 34,
}

with open("js.json", "w", encoding="utf-8") as file:
    json.dump(student, file, ensure_ascii=False, indent=4)

with open("js.json", "r", encoding="utf-8") as file:
    p = json.load(file)
print(f"Загруженный словарь: {p}")

print("\n" + "="*50 + "\n")


#ПРИМЕР 2: Класс User с сериализацией
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        """Преобразует объект User в словарь для JSON сериализации"""
        return {
            "name": self.name,
            "age": self.age,
        }

    @classmethod
    def from_dict(cls, data):
        """Создает объект User из словаря, полученного из JSON"""
        return cls(
            name=data["name"],
            age=data["age"],
        )
    
    def __str__(self):
        return f"User(name='{self.name}', age={self.age})"


# Создаем пользователя и сохраняем в JSON
user1 = User("Таня", 17)
print(f"Создан пользователь: {user1}")

with open("js.json", "w", encoding="utf-8") as file:
    json.dump(user1.to_dict(), file, ensure_ascii=False, indent=4)

# Загружаем из JSON и восстанавливаем объект
with open("js.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

loaded_user = User.from_dict(loaded_data)
print(f"Загруженный пользователь: {loaded_user}")
print(f"Данные загруженного пользователя: имя={loaded_user.name}, возраст={loaded_user.age}")

print("\n" + "="*50 + "\n")


#ПРИМЕР 3: Демонстрация содержимого JSON файла
with open("js.json", "r", encoding="utf-8") as file:
    file_content = file.read()
    print(f"Содержимое js.json:\n{file_content}")

print("\n" + "="*50 + "\n")


#ПРИМЕР 4: Работа с несколькими пользователями
users = [
    User("Анна", 25),
    User("Иван", 30),
    User("Мария", 22),
    User("рая", 17)  # из пятого примера
]

# Сохраняем список пользователей
users_dicts = [user.to_dict() for user in users]
with open("users.json", "w", encoding="utf-8") as file:
    json.dump(users_dicts, file, ensure_ascii=False, indent=4)

# Загружаем список пользователей
with open("users.json", "r", encoding="utf-8") as file:
    loaded_users_data = json.load(file)

loaded_users = [User.from_dict(user_data) for user_data in loaded_users_data]

print("Загруженные пользователи:")
for i, user in enumerate(loaded_users, 1):
    print(f"  {i}. {user}")

print("\n" + "="*50 + "\n")


#ПРИМЕР 5: Демонстрация проблемы прямой сериализации
print("Попытка сериализовать объект User напрямую вызовет ошибку:")
print('''
# Этот код НЕ РАБОТАЕТ:
# with open("error.json", "w", encoding="utf-8") as file:
#     json.dump(User("ТАНЯ", 17), file, ensure_ascii=False, indent=4)
''')
print("Ошибка: Object of type User is not JSON serializable")
print("Решение: использовать метод to_dict() для преобразования в словарь")


#ДОПОЛНИТЕЛЬНО: Чтение созданных файлов
import os

for filename in ["js.json", "users.json"]:
    if os.path.exists(filename):
        size = os.path.getsize(filename)
        print(f"  {filename}: {size} байт")
    else:
        print(f"  {filename}: файл не найден")