import csv
test_csv= [
    ['Имя', 'Возраст', 'Город'],
    ['анна', '30', 'Москва'],
    ['Петр', '34', 'Москва']
]

with open ('test_data_csv', 'w', encoding='utf-8', newline='') as file:
    writer=csv.writer(file)
    writer.writerows(test_csv)

with open('test_data_csv','r', encoding='utf-8', newline='') as file:
    writer=csv.writer(file)
    writer.writerows (test_csv)

with open( 'test_data_csv', 'r' ,encoding='utf-8') as file:
    reader=csv. reader (file)
    for row_num, row in enumerate (reader, 1):
        print(f'Строка {row_num}: {row}')
        print(f'Строка {type(row) }')

with open( 'test_data_csv', 'r', encoding='utf-8') as file:
    reader=csv.DictReader (file)
    for i in reader:
      print(f'{row['Имя']}, Возраст: {row['Возраст']}, Город: {row['Город']}')
      print(f" Тип: {type (row) }")



import json

test_json = {
    "Имя": "Анна",
    "Возраст": 30,
    "Город": "Москва"
}

with open('test_data_json', 'w', encoding = 'utf-8') as file:
    json.dump(test_json, file, ensure_ascii = False, indent = 2)

with open( 'test_data_csv', 'r', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)
    print(f"Данные: {data}")
    print(f"Тип: {type(data)}")
    print(f"Имя: {data['Имя']}")
    