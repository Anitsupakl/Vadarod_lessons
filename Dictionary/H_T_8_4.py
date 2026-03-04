#Создайте следующий словарь: ключи– BMW, Tesla; значения– список из 3х моделей.
#Выведите 1ое и последнее значения каждого из ключей

dictionary = {
    'BMW': ['M5', 'X5', 'X6'],
    'Tesla': ['Cybertruck', 'Y', 'X']
}

for key, values in dictionary.items():
    print(key, values[0], values[-1])