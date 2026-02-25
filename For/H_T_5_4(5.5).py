#Переписать задачи 5.4, 5.5., 5.7, чтобы на вход получался список с использованием генератора списков

#5.5
#Вход: 2 числа a и b Программа выводит все четные числа на промежутке от a до b

number_a = int(input())
number_b = int(input())


number_list = [i for i in range(number_a, number_b) if i % 2 == 0]
print(number_list)