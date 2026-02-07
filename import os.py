import os
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def info(self):
        pass

class Book:
    def __init__(self, title, author):
        self._title = title
        self._author = author
        self._status = "доступна"
    
    @property
    def title(self): return self._title
    @property
    def author(self): return self._author
    @property
    def status(self): return self._status
    
    @status.setter
    def status(self, value):
        if value in ["доступна", "выдана"]:
            self._status = value
    
    def __str__(self):
        return f"{self._title} ({self._author}) - {self._status}"

class User(Person):
    def __init__(self, name):
        self._name = name
        self._books = []
    
    @property
    def name(self): return self._name
    @property
    def books(self): return self._books
    
    def info(self):
        return f"Пользователь: {self._name}"
    
    def take_book(self, title):
        self._books.append(title)
    
    def return_book(self, title):
        if title in self._books:
            self._books.remove(title)
            return True
        return False

class Librarian(Person):
    def __init__(self, name):
        self._name = name
    
    def info(self):
        return f"Библиотекарь: {self._name}"

class Library:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.load_data()
    
    # ================ РАБОТА С ФАЙЛАМИ ================
    def save(self):
        with open("books.txt", "w", encoding='utf-8') as f:
            for b in self.books.values():
                f.write(f"{b.title};{b.author};{b.status}\n")
        with open("users.txt", "w", encoding='utf-8') as f:
            for u in self.users.values():
                f.write(f"{u.name};{','.join(u.books)}\n")
    
    def load_data(self):
        if os.path.exists("books.txt"):
            with open("books.txt", "r", encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        t, a, s = line.strip().split(';')
                        book = Book(t, a)
                        book.status = s
                        self.books[t] = book
        
        if os.path.exists("users.txt"):
            with open("users.txt", "r", encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        name, books_str = line.strip().split(';')
                        user = User(name)
                        if books_str:
                            for title in books_str.split(','):
                                user.take_book(title)
                                if title in self.books:
                                    self.books[title].status = "выдана"
                        self.users[name] = user
    
    # ================ ФУНКЦИИ БИБЛИОТЕКАРЯ ================
    def add_book(self):
        t = input("Название: ")
        if t in self.books:
            print("Книга уже есть!")
            return
        a = input("Автор: ")
        self.books[t] = Book(t, a)
        print("Книга добавлена!")
    
    def remove_book(self):
        t = input("Название для удаления: ")
        if t in self.books:
            del self.books[t]
            print("Книга удалена!")
        else:
            print("Книга не найдена")
    
    def add_user(self):
        name = input("Имя нового пользователя: ")
        if name not in self.users:
            self.users[name] = User(name)
            print("Пользователь добавлен!")
        else:
            print("Пользователь уже есть")
    
    def show_users(self):
        print("\nВСЕ ПОЛЬЗОВАТЕЛИ")
        if not self.users:
            print("Пользователей нет")
        for u in self.users.values():
            print(f"- {u.info()}")
    
    def show_all_books(self):
        print("\nВСЕ КНИГИ")
        if not self.books:
            print("Книг нет")
        for b in self.books.values():
            print(f"- {b}")
    
    # ================ ФУНКЦИИ ПОЛЬЗОВАТЕЛЯ ================
    def show_available(self):
        print("\n=== ДОСТУПНЫЕ КНИГИ ===")
        available = [b for b in self.books.values() if b.status == "доступна"]
        if not available:
            print("Нет доступных книг")
            return []
        for i, b in enumerate(available, 1):
            print(f"{i}. {b.title} - {b.author}")
        return available
    
    def take_book_for_user(self, user_name):
        if user_name not in self.users:
            print("Ошибка: пользователь не найден")
            return
        
        available = [b for b in self.books.values() if b.status == "доступна"]
        if not available:
            print("Нет доступных книг")
            return
        
        print("Доступные книги:")
        for i, b in enumerate(available, 1):
            print(f"{i}. {b.title} - {b.author}")
        
        try:
            num = int(input("Номер книги: ")) - 1
            if 0 <= num < len(available):
                book = available[num]
                book.status = "выдана"
                self.users[user_name].take_book(book.title)
                print(f"Вы взяли: {book.title}")
        except:
            print("Ошибка ввода")
    
    def return_book_user(self, user_name):
        if user_name not in self.users:
            print("Ошибка: пользователь не найден")
            return
        
        user = self.users[user_name]
        if not user.books:
            print("У вас нет книг")
            return
        
        print("Ваши книги:")
        for i, title in enumerate(user.books, 1):
            print(f"{i}. {title}")
        
        try:
            num = int(input("Номер для возврата: ")) - 1
            if 0 <= num < len(user.books):
                title = user.books[num]
                if user.return_book(title):
                    if title in self.books:
                        self.books[title].status = "доступна"
                    print("Книга возвращена!")
        except:
            print("Ошибка ввода")
    
    def show_user_books(self, user_name):
        if user_name in self.users:
            user = self.users[user_name]
            print(f"\n=== ВАШИ КНИГИ ===")
            if user.books:
                for i, title in enumerate(user.books, 1):
                    print(f"{i}. {title}")
            else:
                print("Нет книг")

def main():
    lib = Library()
    
    print("БИБЛИОТЕЧНАЯ СИСТЕМА")
    print("1. Библиотекарь")
    print("2. Пользователь")
    role_choice = input("Выберите роль: ")
    
    if role_choice == "1":
        while True:
            print("\nМЕНЮ БИБЛИОТЕКАРЯ")
            print("1. Добавить книгу")
            print("2. Удалить книгу")
            print("3. Добавить пользователя")
            print("4. Список пользователей")
            print("5. Список всех книг")
            print("6. Завершить работу")
            
            choice = input()
            
            if choice == "1":
                lib.add_book()
            elif choice == "2":
                lib.remove_book()
            elif choice == "3":
                lib.add_user()
            elif choice == "4":
                lib.show_users()
            elif choice == "5":
                lib.show_all_books()
            elif choice == "6":
                lib.save()
                print("Работа завершена. Данные сохранены.")
                break
    
    elif role_choice == "2":
        name = input("Введите ваше имя: ")
        
        if name not in lib.users:
            print("Ошибка: пользователь не найден. Обратитесь к библиотекарю.")
            return
        
        while True:
            print(f"\nМЕНЮ ПОЛЬЗОВАТЕЛЯ ({name})")
            print("1. Доступные книги")
            print("2. Взять книгу")
            print("3. Вернуть книгу")
            print("4. Мои книги")
            print("5. Выйти")
            
            choice = input()
            
            if choice == "1":
                lib.show_available()
            elif choice == "2":
                lib.take_book_for_user(name)
            elif choice == "3":
                lib.return_book_user(name)
            elif choice == "4":
                lib.show_user_books(name)
            elif choice == "5":
                lib.save()
                print("Выход. Данные сохранены.")
                break

if __name__ == "__main__":
    main()