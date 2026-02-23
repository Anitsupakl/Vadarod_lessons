#На вход программа принимает 2 строки и выводит все символы из второй  строки, которых нет в первой

variable_1, variable_2 = input(), input()

made_set_1 = set(variable_1)
made_set_2 = set(variable_2)

common_set = made_set_2.difference(made_set_1)
print(common_set)