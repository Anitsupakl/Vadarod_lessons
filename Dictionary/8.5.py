#Пол, Анна и Алекс писали контрольную. Пол и Анна получили 4, а умничка Алекс 5.
# Напишите программу, которая по имени показывает оценку. На вход программа получает имя

name_input = input().capitalize()

dictionary = {'Пол': 4, 'Анна': 4, 'Алекс': 5}

for name, mark in dictionary.items():
    if name_input == name:
        print(f'Оценка {name} - {mark}')

