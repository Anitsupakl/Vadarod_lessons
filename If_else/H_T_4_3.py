#Написать простой калькулятор: сложение, вычитание, деление, умножение. Программа в зависимости от действия с двумя введенными пользователем числами выводит результат.

number_1 = int(input())
number_2 = int(input())

print('Enter method:','+', '-', '/', '*')
enter_method = input()
if enter_method == '+':
    print(number_1 + number_2)
elif enter_method == '-':
    print(number_1 - number_2)
elif enter_method == '/':
    print(number_1 / number_2)
elif enter_method == '*':
    print(number_1 * number_2)






