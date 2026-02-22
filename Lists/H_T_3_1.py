#Вход: разные слова. Программа создает из них список и выводит его задом наперед

words = (input(), input(), input(), input(), input())
words = list(words)
words.reverse()

print(words)