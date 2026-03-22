#Прочитать из файла числа, сформировать список и напечатать его Out: [10, 91, 76, 48, 11, 89, 65, 56, 81, 94, 36]

#with (open('C:\\Users\\valeriya.kapustina\\Desktop\\Files_train\\10_2.txt', 'r') as file):
#    text = file.read()
#    numbers_list = []
#    for numbers in file:
#        numbers_join = numbers.split(' ')
#        numbers_list.append(numbers_join)
#with (open('C:\\Users\\valeriya.kapustina\\Desktop\\Files_train\\10_2.txt', 'a') as file):
#    for number in numbers_list:
#        text = file.write(number + '\n')
#print(text)


numbers = []
with open('D:\Lessons_vadarod\\10_2.txt', 'r') as f:
    for line in f:
        numbers.append(int(line.strip()))

print(numbers)
# [10, 91, 76, 48, 11, 89, 65, 56, 81, 94, 36]