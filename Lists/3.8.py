#Вход: список
#['dog', 'cat', 'rat', 'rabbit'].
#Программа делает из него список
#['rat', 'rabbit', 'pig', 'dog', 'cat']

animals = ['dog', 'cat', 'rat', 'rabbit']
animals.insert(2, 'pig')
animals.sort(reverse=True)
print(animals)








