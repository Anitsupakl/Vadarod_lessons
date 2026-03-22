#Напишите функцию которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
# а чётные нацело делит на два. In: 852 85 784 58 Out: [852, 784, 58]

def numbers_list(number_list : list) -> list:
    integer_number_list = []
    for numbers in number_list:
        if numbers % 2 == 0:
            integer_number_list.append(numbers)
    integer_number_list = [i // 2 for i in integer_number_list]

    return integer_number_list

print(numbers_list(number_list=[120,240,3,4,5,6,7,8,9]))
