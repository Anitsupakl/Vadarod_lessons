#Создать словарь, ключи — числа, значения — слова.
# Удалить из него все пары с нечетными ключами.
# Вывести на печать В этом вам может помочь статья, что сбрасывала ранее.

dictionary = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five'
}
#for key, values in dictionary.items():
#    if key % 2 != 0:
#        del dictionary[key]
new_dictionary = {key: value for key, value in dictionary.items() if key % 2 == 0}
print(new_dictionary)
