#ана строка 'rythm rough rush shake than’. Программа выводит строку, в которой все
#буквы ‘h’ заменены на ‘H’, кроме первого и последнего вхождений.

variable = 'rythm rough rush shake than'
variable_first_part = variable[:variable.find('h') + 1]
variable_second_part = variable.replace('h', 'H')[variable.find('h') + 1:variable.rfind('h')]
variable_third_part = variable[variable.rfind('h'):]

print(variable_first_part + variable_second_part + variable_third_part)

