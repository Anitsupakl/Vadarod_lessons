#Вход: 2 слова. Программа проверяет являются ли они анаграммой (из одного слова можносоставить другое). Если да– вывести ‘anagram’, если нет– ‘just words’.
# Sorted(variable)

word_1, word_2 = input(), input()

print(sorted(word_1), sorted(word_2))

if sorted(word_1) == sorted(word_2):
    print("anagram")
else:
    print("just words")