import json
from collections import Counter, defaultdict

with open("orders_july_2023.json", "r", encoding="utf-8") as f:
    orders = json.load(f)
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

max_price = 0
max_price_order = ''

max_quantity = 0
max_quantity_order = ''

orders_per_day = Counter()
orders_per_user = Counter()
total_price_per_user = defaultdict(float)

total_price_all = 0
total_quantity_all = 0
total_orders = 0

# Обработка каждого заказа
for order_num, data in orders.items():
    price = data['price']
    quantity = data['quantity']
    date = data['date']
    user_id = data['user_id']

    # Максимальная стоимость заказа
    if price > max_price:
        max_price = price
        max_price_order = order_num

    # Максимальное количество товаров в заказе
    if quantity > max_quantity:
        max_quantity = quantity
        max_quantity_order = order_num

    # Количество заказов по дням
    orders_per_day[date] += 1

    # Количество заказов и суммарная стоимость по пользователям
    orders_per_user[user_id] += 1
    total_price_per_user[user_id] += price

    # Общая сумма и количество
    total_price_all += price
    total_quantity_all += quantity
    total_orders += 1

# День с максимальным количеством заказов
max_orders_day, max_orders_count = orders_per_day.most_common(1)[0]

# Пользователь с максимальным количеством заказов
max_orders_user, max_user_orders_count = orders_per_user.most_common(1)[0]

# Пользователь с максимальной суммарной стоимостью заказов
max_price_user = max(total_price_per_user, key=total_price_per_user.get)
max_user_total_price = total_price_per_user[max_price_user]

# Средняя стоимость заказа и товара
avg_order_price = total_price_all / total_orders if total_orders else 0
avg_item_price = total_price_all / total_quantity_all if total_quantity_all else 0

# Вывод результатов
print(f"Номер самого дорогого заказа в июле: {max_price_order} (стоимость {max_price})")
print(f"Номер заказа с самым большим количеством товаров: {max_quantity_order} (товаров {max_quantity})")
print(f"День с наибольшим количеством заказов в июле: {max_orders_day} (заказов {max_orders_count})")
print(f"Пользователь с самым большим количеством заказов в июле: {max_orders_user} (заказов {max_user_orders_count})")
print(
    f"Пользователь с самой большой суммарной стоимостью заказов в июле: {max_price_user} (сумма {max_user_total_price})")
print(f"Средняя стоимость заказа в июле: {avg_order_price:.2f}")
print(f"Средняя стоимость товара в июле: {avg_item_price:.2f}")
