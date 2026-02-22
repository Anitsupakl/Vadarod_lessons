#Вход: число 0. Программа
#создает список, заполненный
#нулями, кроме первого и
#последнего элементов.

number = 0
number_to_str = str(number)
number_to_list = list(number_to_str * 5)
number_to_list[0] = '-'
number_to_list[len(number_to_list) - 1] = '-'

print(number_to_list)