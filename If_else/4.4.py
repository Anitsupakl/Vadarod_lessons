#Вход: возраст пользователя. Если пользователь строго меньше 18 лет, программа выводит ‘Coca cola’.
# Если пользователю 0 лет, то выводит ‘Wrong age’ В другом случае программа выводит ‘Beer

age = int(input())

if age < 18:
    print('Coca cola')
elif age == 0:
    print('Wrong age')
else:
    print('Beer')