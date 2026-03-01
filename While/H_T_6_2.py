#Определите кол-во отрицательных и положительных элементов последовательности, заканчивающейся числом 0.

#sequence = [-1000000, 1000000]
#count_numbers_end_zero = 0
#for i in range(sequence[0], sequence[1]):
#    if i % 5 == 0 and i % 2 == 0:
#        count_numbers_end_zero += 1
#print(count_numbers_end_zero)

pozitive_numbers = 0
negative_numbers = 0

number = int(input('Enter the number \n'))

while number != 0:
    if number > 0 and number % 10 == 0:
        pozitive_numbers += 1
    elif number < 0 and number % 10 == 0:
        negative_numbers += 1
    number = int(input('Enter number again \n'))


print(pozitive_numbers)
print(negative_numbers)



