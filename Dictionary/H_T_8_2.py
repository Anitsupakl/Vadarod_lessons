#Программа принимает список из трех слов. Создать словарь,
# в котором ключ — слово, значение — количество символов в слове
three_words = []
for i in range(3):
    words = input()
    three_words.append(words)

dictionary = {d: len(d) for d in three_words}
print(dictionary)
