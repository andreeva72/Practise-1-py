import os
import pickle
import json
import gzip
from dataclasses import dataclass, asdict

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(5, 6)

print(type(p))
massiv = pickle.dumps(p)
print(type(massiv))
from_massiv = pickle.loads(massiv)
print(type(from_massiv))
print(from_massiv.x)
print(from_massiv.y)

class User:
    def __init__(self, login, passw):
        self.login = login
        self.password = passw

    def __getstate__(self):
        state = self.__dict__.copy()
        del state["password"]
        state["version"] = 1
        return state

    def __setstate__(self, state):
        version = state.pop("version", None)
        self.__dict__.update(state)
        self.password = ""

user = User("123@mail.ru", 123)

with open("p8.pkl", "wb") as file:
    pickle.dump(user, file)

with open("p8.pkl", "rb") as file:
    user1 = pickle.load(file)

print(user.login, user.password)
print(user1.login, user1.password)

print("\n=== 3. Group и Student ===\n")

class Group:
    def __init__(self, name):
        self.name = name

class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

group = Group("n1-24")
st = Student("Даня", group)

obj = pickle.dumps(st)
new_obj = pickle.loads(obj)
print(new_obj.name, new_obj.group.name)

print("\n=== 4. User с JSON ===\n")

class UserJSON:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age
        }

    @staticmethod
    def from_dict(st):
        return UserJSON(
            name=st["name"],
            age=st["age"]
        )

def to_default(obj):
    if isinstance(obj, UserJSON):
        return obj.to_dict()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

user_json = UserJSON("Тана", 17)

with open("js.json", "w", encoding="utf-8") as file:
    json.dump(user_json, file, default=to_default, ensure_ascii=False, indent=4)

with open("js.json", "r", encoding="utf-8") as file:
    p = json.load(file)

user_loaded = UserJSON.from_dict(p)
print(user_loaded.name, user_loaded.age)
print(user_loaded.age, user_loaded.name)

class StudentJSON:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "grades": self.grades
        }

    @staticmethod
    def from_dict(st):
        return StudentJSON(
            name=st["name"],
            age=st["age"],
            grades=st["grades"]
        )

def to_default_student(obj):
    if isinstance(obj, StudentJSON):
        return obj.to_dict()
    raise TypeError(f"Объект не может быть сериализован в json")

student = StudentJSON("g", 40, [4, 2, 3])

with open("st8.json", "w", encoding="utf-8") as file:
    json.dump(student, file, default=to_default_student, ensure_ascii=False, indent=2)

with open("st8.json", "r", encoding="utf-8") as file:
    f = json.load(file)

loaded_student = StudentJSON.from_dict(f)
print(loaded_student.name, loaded_student.age, loaded_student.grades)

print("\n=== 6. Dataclass ===\n")

@dataclass
class StudentDC:
    name: str
    age: int
    grades: list

student_dc = StudentDC("g", 40, [4, 2, 3])

st_to_dict = asdict(student_dc)

with open("st8_dc.json", "w", encoding="utf-8") as file:
    json.dump(st_to, file, ensure_ascii=False, indent=2)

with open("st8_dc.json", "r", encoding="utf-8") as file:
    f = json.load(file)

st1 = StudentDC(**f)
print(st1.name, st1.age, st1.grades)

class PointList:
    def __init__(self, x, y):
        self.x = x
        self.y = y

points = [PointList(3, 5), PointList(3, 4), PointList(5, 6)]

with open("point5.pkl", "wb") as file:
    pickle.dump(points, file, protocol=4)

with open("point5.pkl", "rb") as file:
    a = pickle.load(file)

for i in a:
    print(i.x, i.y)