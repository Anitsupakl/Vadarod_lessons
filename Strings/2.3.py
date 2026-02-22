#Вход:
#возраст
#переменная, имя и фамилия– 2переменная.
#Проверить равно ли кол-во
#элементов 2ой переменной
#числу в 1ой.
#Оператор равенства ==

age = int(input('Enter the age \n'))
name_and_surname = input('Enter your name and surname \n')

print(len(name_and_surname) == age)