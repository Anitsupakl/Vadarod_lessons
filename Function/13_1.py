#Из полученного списка чисел создайте список с суммами этих чисел, отсортированными по возрастанию In: 965 582 023 8 695210 Out: [5, 8, 15, 20, 23]

def numbers_list(*numbers) -> list:
    numbers_sorted = sorted(numbers)

    return numbers_sorted

print(numbers_list(12,15,13,14,89,2,3,17))
