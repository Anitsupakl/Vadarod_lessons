#Придумать задачу для использования методов строк. Минимум 2– 3 метода. Задача должна содержать условие и Ваше решение

#При регистрации на сайте пользователь ввёл пароль: "пароль123".
#Программа должна проверить, соответствует ли пароль требованиям безопасности
#Требования к паролю:
#Длина не менее 8 символов
#Не содержит пробелов

password = ' pass123'
password_len = len(password)
print(password_len >= 8)
password_is_upper = password.isupper()
print(password_is_upper)
space_in_password = password.strip()
print(space_in_password)



