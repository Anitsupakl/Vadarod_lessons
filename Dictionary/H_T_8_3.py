#На вход подается список чисел. Создать словарь, в котором ключ — число,
# значение —число на 10% больше. Значение должно быть округленное.

numbers_list = []
numbers = list(input())
for i in numbers:
    i = int(i)
    numbers_list.append(i)

dictionary = {d: round(d*0.1 + d) for d in numbers_list}



print(dictionary)




