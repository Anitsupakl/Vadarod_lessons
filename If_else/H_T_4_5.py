#Проверить почту на наличие собаки и вывести сообщение

emails = [
    "user@gmail.com",
    "admin@company.ru",
    "invalid-email",]
new_emails_without_symbol =[]
if '@' not in emails:
    new_emails_without_symbol.append('Есть адреса без собаки, но какие ищите сами')

print(new_emails_without_symbol)

del emails[:]
print('Напишите нормальные почты')





