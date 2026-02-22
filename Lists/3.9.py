#Вход: список
#[1, 2, 3, 4, 5]
#Программа создает такой же
#список из этого, удалет в нем
#все элементы со 2го до
#последнего. Проверяет, что это
#разные списки

numbers = [1, 2, 3, 4, 5]
numbers_2 = numbers.copy()

print(numbers_2.pop(-1))
print(numbers_2.pop(-1))
print(numbers_2.pop(-1))
print(numbers == numbers_2)

