#Вход: температура и вид градусов. Программа переводит из Цельсия в Фаренгейты и наоборот

temperature = int(input())
temperature_type = input()

if 'c' in temperature_type:
    print(f'В {temperature} градусов Цельсия {(temperature * 1.8 + 32)} градусов по Фаренгейту')
elif 'f' in temperature_type:
    print(f'В {temperature} градусов по Фаренгейту {(temperature - 32) / 1.8} градусов Цельсия')

