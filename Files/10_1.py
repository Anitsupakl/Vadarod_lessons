#Создать список из 10 случайных чисел. Записать в файл:
# 1.Количество элементов в списке
# 2. Все элементы списка в одну строку Т.е. в файле должно быть 2 строки

import random
random_numbers = [random.randint(0, 20) for number in range(11)]
with (open('D:\\Lessons_vadarod\\Files\\10_1.txt', 'w') as file):
    text = str(len(random_numbers))
    file.write(f'Количество элементов в списке: {text}' + '\n')

with open('D:\\Lessons_vadarod\\Files\\10_1.txt', 'a') as file:
    for text in random_numbers:
        text = str(text)
        file.write(text + ' ')

with open('D:\\Lessons_vadarod\\Files\\10_1.txt', 'r') as file:
    text = file.read()

print(text)
