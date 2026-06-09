import requests
import time
import requests
import asyncio
import aiohttp
import threading

#Синхронное скачивание (из IMG_1687, IMG_1688)
print("начинаю скачивать первое изображение")
response = requests.get("https://static.tildacdn.com/tild6139-3466-4433-a564-316666376137/PPu1wH0hqDA.jpg")
print("скачалось первое изображение")
print("начинаю скачивать второе изображение")
response1 = requests.get("https://static.tildacdn.com/tild6139-3466-4433-a564-316666376137/PPu1wH0hqDA.jpg")
print("скачалось второе изображение")
print(response.status_code)

#Асинхронная функция hello (из IMG_1689, IMG_1690, IMG_1691)
async def hello():
    print("Привет")
    await asyncio.sleep(2)
    print("Н1-24")

async def main_hello():
    task1 = asyncio.create_task(hello())
    task2 = asyncio.create_task(hello())
    await task1
    await task2

#Асинхронное скачивание (из IMG_1692, IMG_1694)
async def download(session, url, name):
    print(f"начинаю скачивать изображение {name}")
    async with session.get(url) as response:
        image_data = await response.read()
        print(f"Изображение скачалось {name}")
        return image_data

async def main_download():
    async with aiohttp.ClientSession() as session:
        task1 = download(session, "https://static.tildacdn.com/tild6139-3466-4433-a564-316666376137/PPu1wH0hqDA.jpg", "Картинка 1")
        task2 = download(session, "https://static.tildacdn.com/tild6139-3466-4433-a564-316666376137/PPu1wH0hqDA.jpg", "Картинка 2")
        task3 = download(session, "https://static.tildacdn.com/tild6139-3466-4433-a564-316666376137/PPu1wH0hqDA.jpg", "Картинка 3")
        await asyncio.gather(task1, task2, task3)

#Многопоточность (из IMG_1696)
def make_coffee():
    print("Начали варить кофе")
    time.sleep(2)
    print("Окончание варить кофе")

def eggs():
    print("Начали варить яйцо")
    time.sleep(2)
    print("Окончание варить яйцо")

#Запуск всех примеров
if __name__ == "__main__":
    print("\nПример с time.sleep")
    print("Начало процесса")
    time.sleep(2)
    print("Окончание процесса")
    
    print("\nПример с потоками (threading)")
    t1 = threading.Thread(target=make_coffee)
    t2 = threading.Thread(target=eggs)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print("\nПример с asyncio hello")
    asyncio.run(main_hello())
    
    print("\nПример с асинхронным скачиванием")
    asyncio.run(main_download())
