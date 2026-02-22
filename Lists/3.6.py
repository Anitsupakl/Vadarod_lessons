#Вход: список
#['cat', 'rabbit', 'elephant’]
#Программа делает из него 2 списка:
#1. Содержит животное и колво букв в его имени
#2. Содержит животных, где последняя буквы заглавная

animals = ['cat', 'rabbit', 'elephant']
animals_first_list = (animals[0], len(animals[0]), animals[1], len(animals[1]), animals[2], len(animals[2]))

animals_second_list_upper = [(animals[0][::-1]).capitalize(), animals[1][::-1].capitalize(),animals[2][::-1].capitalize()]
animals_second_list = [animals_second_list_upper[0][::-1], animals_second_list_upper[1][::-1],animals_second_list_upper[2][::-1]]
print(animals_first_list)
print(animals_second_list)








