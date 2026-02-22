#Вход: беспорядочный набор символов, например: ade rg gt5 re u. Заменить пробелы на
#* ипосчитать сколько получилось *

variable = input()
variable_2 = variable.replace(' ', '*')
variable_count = variable_2.count('*')

print(variable_count)