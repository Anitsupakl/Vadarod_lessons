#Вход: целое число N. Определить является ли оно простым.
# Число называется простым, если у него есть только 2 делителя: единица и само число N


number = int(input())

if number <= 1:
    print(f"{number} не простое")
else:
    delitel = 2
    while delitel < number:
        if number % 2 == 0:
            print('у чсла больше 2 делителей')
            break
        else:
            print('Число простое')
            break

