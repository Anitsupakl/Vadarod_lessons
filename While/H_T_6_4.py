#Джон пошел в магазин тратить зарплату ZP и покупает все, что попадется под руку.
# Напишите программу, которая скажет «Стоп, Джон!» в тот момент, когда, с добавением нового товара в торзину,
# итоговая стоимость будет больше ZP. И в конце вывести сколько денег осталось у Джона


john_salary_start = 6000
john_salary_with_product = 6000
products = 0
all_products = 0
while john_salary_start > all_products:
    products = int(input('Стоимость продукта \n'))
    if all_products > john_salary_start:
        print('Стоп Джон')
    print(f'стоимость продукта {products}')
    john_salary_with_product -= products
    print(f'осталось деняк {john_salary_with_product}')
    all_products += products
    print(f'стоимость всех продуктов {all_products}')

john_salary_end = john_salary_start - all_products
if john_salary_end < 0:
    print(f'У нас долг  {john_salary_end} баксов')
