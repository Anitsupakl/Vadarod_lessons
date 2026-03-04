#Дан словарь: dic = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
# Выведите на экран произведение всех значений словаря.

dic = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}

product = 1

for values in dic.values():
    product *= values

print(product)