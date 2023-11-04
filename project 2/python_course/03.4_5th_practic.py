import csv
import os
import time

list_ = [
    {
        'name': 'Masha', 'age': 25, 'job': 'Scientist'
    },
    {
        'name': 'Vasya', 'age': 26, 'job': 'Programmer'
    },
    {
        'name': 'Misha', 'age': 45, 'job': 'Boss'
    }
        ]

with open('result.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        {
            'name', 'age', 'job'
        }
    )

with open('result.csv', 'a', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    for el in list_:
        name = el["name"]
        age = el['age']
        job = el['job']
        writer.writerow(
            [
                name, age, job
            ]
        )
time.sleep(15)
os.remove('result.csv')