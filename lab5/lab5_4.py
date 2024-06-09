#(задача 4) Написать программу на Python преобразующую
#json файл  в CSV. Входной параметр  – имя json файла.
#Результирующий CSV файл должен иметь название из названия
#корневой записи json и размещаться  в той же папке что и  json.
#Формат вызова программы в командной строке:  json2csv.py example.json

import json
import csv
import os

with open('employees.json', 'r') as j:
    json_data = json.load(j)#json -> py
    #print(json_data)
    employee = list(json_data.keys())[0]
    #print(employee)
    file_j = os.path.splitext('employees.json')[0] + '-' + employee + '.csv'

with open(file_j, 'w', newline='') as c:
    file_c = csv.writer(c)
    
    title = list(json_data[employee][0].keys())
    file_c.writerow(title)
    
    for i in json_data[employee]:
        file_c.writerow([i[j] for j in title])
