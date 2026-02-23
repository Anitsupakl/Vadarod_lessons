#Вход: 2 строки. Программа проверяет входит ли одна строка во вторую. Если да, то выводит “I’m here’, если нет, то “I’m not here

first_variable = input()
second_variable = input()

if first_variable in second_variable:
    print('I\'m here')
else:
    print('I\'m not here')