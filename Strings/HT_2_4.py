#ана строка 'rythm rough rush shake than’. Программа выводит строку, в которой
#последовательность символов между перым и последним появлением буквы ‘h’
#повернута в противоположном порядке

variable = 'rythm (rough rush shake) than'

variable_2=(variable[variable.find('h'):variable.rfind('h') + 1])

print(variable_2[::-1])

