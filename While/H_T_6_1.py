#Определите сумму элементов, кратных 5, последовательности, заканчивающейся числом 0.

end_number = 0
elements_sum = 0
while end_number < 1000:
    if end_number % 5 == 0 and end_number % 2 == 0:
        elements_sum += end_number
    end_number += 1

print(f'Сумма {elements_sum}')

