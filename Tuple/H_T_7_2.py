#Создайте кортеж из 5 случайных чисел от 1 до 10. Все числа, кроме первого и последнего, распаковать в один список. Для распаковки используйте *

first_tuple = 1,4,5,7,9

#a,b,c = (first_tuple[1:len(first_tuple) - 1])

first, *middle, last = first_tuple
print(*middle)