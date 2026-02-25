#Вход: список чисел. Программа строить диаграмму из *

numbers = input('Введите числа через пробэл\n').split(' ')
numbers = list(numbers)

for i in numbers:
    print(int(i) * '*')
