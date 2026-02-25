#Вход: 2 числа a и b Программа выводит все четные числа на промежутке от a до b

number_a = int(input())
number_b = int(input())

for i in range(number_a, number_b + 1):
   if i % 2 == 0:
       print(i)