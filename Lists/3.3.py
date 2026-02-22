#Вход: 2 слова. Программа
#создает из них 2 списка:
#1. Содержит все буквы;
#2. Содержит все слова

words = input(),input()
first_list = list(','.join(words).replace(',', ''))
second_list = list(words)
print(first_list)
print(second_list)

