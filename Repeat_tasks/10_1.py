#Дан словарь ключ- значение. Нужно считать содержимое в список так, чтобы сначала шли числа по возрастанию,
# а потом слова по возрастанию их длинны. Dict = {“python”:4, “java”:7, “data”: 14, 6 : “game”, 1 : “film”}

Dict = {'python':4, 'java':7, 'data': 14, 6 : 'game', 1 : 'film'}
numbers = []
words = []

for num, wrd in Dict.items():
    if type(num) is int and type(wrd) is str:
        numbers.append(num)
        words.append(wrd)
    elif type(num) is str and type(wrd) is int:
        numbers.append(wrd)
        words.append(num)
numbers = sorted(numbers)
words = sorted(words)

print(numbers)
print(words)

finish_dictinary = dict(zip(numbers, words))
print(finish_dictinary)