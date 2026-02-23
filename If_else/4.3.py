#Вход: кол-во какое-то символов. В случае, если кол-во символов четное, программа выводит ‘even’. Если нечетное: ‘odd


variable = input()

if len(variable) % 2 == 0:
    print('even')
else:
    print('odd')
