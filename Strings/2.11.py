#оздать переменную ‘Anna
#loves music! She plays the
#piano very well! Look!’
#Программа должна разделить
#предложения. Не потеряйте
#восклицательный знак!

variable = 'Anna loves music! She plays the piano very well! Look!'

variable_2 = (variable.replace('!', ' !'))

print(variable_2.split(' '))
