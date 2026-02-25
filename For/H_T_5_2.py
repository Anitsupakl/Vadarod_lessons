#Вход: целое число до 15. Программа выводит лесенку из чисел

#number = int(input())
#numbers_list = []
#for i in range(1, number+1):
#    numbers_list.append(i)
#
#    print(numbers_list)

number = int(input())

for i in range(1, number + 1):
    for y in range(1, i + 1):
        print(y, end=' ')
    print()

