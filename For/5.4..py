#5.4
#Вход: 2 числа a и b Программа выводит все числа от a до b включительно. Числа могут быть любыми и подаваться в любом порядке.

number_a = int(input())
number_b = int(input())

if number_a > number_b:
    for i in range(number_b, number_a + 1):
        print(i)
else:
    for i in range(number_a, number_b + 1):
        print(i)