#Вход: [1, 2, 3, 4, 5]
#Программа
#меняет
#местами самый большой и
#самый
#маленький
#элементы.

numbers = [1, 2, 3, 4, 5]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
print(numbers)

