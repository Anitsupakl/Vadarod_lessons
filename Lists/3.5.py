#Вход: список
#['cat', 'dog', 'pig', 'rabbit’].
#Программа делает из него список
#['rat', 'rabbit', 'pig', 'dog', 'cat', 'turtle']
animals = ['cat', 'dog', 'pig', 'rabbit']
del animals[:]
animals.append(['rat', 'rabbit', 'pig', 'dog', 'cat', 'turtle'])

print(animals)

#i don't like this
animals_2 = ['cat', 'dog', 'pig', 'rabbit']
animals_2.append('cat')
animals_2.append('turtle')
animals_2[0] = 'rat'
animals_2[1] = 'rabbit'
animals_2[3] = 'dog'
print(animals_2)


