#На вход программе подаются числа. Создайте кортеж из чисел меньше 5

number_1, number_2, number_3, number_4 = int(input()), int(input()), int(input()), int(input())
empty_list = []
if number_1 < 5:
    empty_list.append(number_1)

if number_2 < 5:
    empty_list.append(number_2)

if number_3 < 5:
    empty_list.append(number_3)

if number_4 < 5:
    empty_list.append(number_4)

print(tuple(empty_list))