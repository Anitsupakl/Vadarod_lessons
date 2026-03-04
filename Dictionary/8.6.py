#Антоха и Димон собрались на рыбалочку. Сначала они пошли в магазин за топливом:
# alco = {'whiskey': 50, 'beer': 5, 'wine': 30, 'vodka': 15}
# Программа принимает сколько у них денег и выводит, что они могут купить. Имеется в виду на выбор, т.е. складывать не надо

alco = {'whiskey': 50, 'beer': 5, 'wine': 30, 'vodka': 15}

money = int(input())
you_can_buy = []

for name_alco, price_alco in alco.items():
    if money >= price_alco:
        you_can_buy.append(name_alco)

print(f'Шота отсюда вы можете купить : {you_can_buy}')
