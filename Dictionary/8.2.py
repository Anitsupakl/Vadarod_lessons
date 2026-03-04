#Создайте словарь из строки 'pythonist’ следующим образом: Ключи–символы строки,
# Значения количество вхождений символа в строку

variable_str = 'pythonist'
variable_list = list(variable_str)

print(variable_list)

dictionary = {d:variable_list.count(d) for d in variable_list}
print(dictionary)
