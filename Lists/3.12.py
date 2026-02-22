#Вход: [1, 2, 3, 4, 5]
#Программа
#заменяет
#наибольший элемент на сумму
#всех элементов. Потом находит
#наименьший и заменяет его на
#сумму элементов


numbers = [1, 2, 3, 4, 5]
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))
numbers[min_index], numbers[max_index] = sum(numbers), sum(numbers)
print(numbers)