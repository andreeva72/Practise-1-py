# import socket
# import threading

# lock = threading.Lock()
# clients = []

# def server_thr(client_socket, client_address):
#     print(f"Клиент {client_address} подключен")
#     while True:
#         data = client_socket.recv(1024)
#         if not data:
#             break
#         message = data.decode("utf-8")
#         print(f"{client_address} отправил: {message}")
    
#     with lock:
#         if client_socket in clients:
#             clients.remove(client_socket)
#     client_socket.close()
#     print(f"Клиент {client_address} отключен")

# socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# socket_server.bind(("127.0.0.1", 5001))
# socket_server.listen()
# print("Сервер запущен и ждет клиентов")

# while True:
#     client_socket, client_addr = socket_server.accept()
#     with lock:
#         clients.append(client_socket)
#     th = threading.Thread(target=server_thr, args=(client_socket, client_addr), daemon=True)
#     th.start()


from threading import Event
from queue import Queue

# queue = Queue(maxsize = 10)

# try:
#     queue.put(item = "", block = False)
# except queue.Full as e:
#     item = queue.get()

# try:
#     queue.get(block = False, timeout = 10)
# except queue.empty:
#     size = queue.size()

# queue.task_done()
# queue.join()

import time
from queue import Empty, Queue
import threading

# def pr(queue):
#     for i in range(1, 6):
#         print(f"Вставляем элемент {i} в очередь")
#         time.sleep(1)
#         queue.put(i)

# def cus(queue): #демонический поток
#     while True:
#         try:
#             item = queue.get()
#         except Empty:
#             continue
#         else:
#             print(f"Обрабатываем элемент {item}")
#             time.sleep(2)
#             queue.task_done()

# def main():
#     queue = Queue()
#     p = threading.Thread(target=pr, args=(queue,))
#     p.start()
#     c = threading.Thread(target=cus, args=(queue,), daemon=True)
#     c.start()

#     p.join()
#     queue.join()

# if __name__ == "__main__":
#     main()

from threading import Thread
from concurrent.futures import ThreadPoolExecutor

from time import sleep, perf_counter

# def task(id):
#     print(f"Начинаю загрузку {id}")
#     sleep(1)
#     return f"Закончили задачу"

# start = perf_counter()

# print(task(1))
# print(task(2))

# fin = perf_counter()
# print(f"Выполнение заняло {fin}")

def task(id):
    print(f"Начинаю загрузку {id}")
    sleep(1)
    return f"Закончили задачу {id}"

start = perf_counter()

with ThreadPoolExecutor() as executor:
    f1 = executor.submit(task, 1)
    f2 = executor.submit(task, 2)
    f3 = executor.submit(task, 3)

print(f1.result())
print(f2.result())
print(f3.result())


fin = perf_counter()
print(f"Выполнение заняло {fin-start}")