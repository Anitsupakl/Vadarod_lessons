#Дана строка 'rythm (rough rush shake) than’. Программа выводит только ту часть строки,
#которая НЕ в скобочках.


variable = 'rythm (rough rush shake) than'

print(variable.replace(variable[variable.find('('): variable.rfind(')') + 1], ''))