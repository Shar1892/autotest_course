# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open("test_file/task_3.txt", "r", encoding="utf-8") as data_file:
    data = data_file.readlines()

    purchase_price = 0
    purchases_list = []
    for row in data:
        if row != '\n':
            purchase_price += int(row)
        else:
            purchases_list.append(purchase_price)
            purchase_price = 0

    purchases_list.sort(reverse=True)

    three_most_expensive_purchases = sum(purchases_list[:3])


assert three_most_expensive_purchases == 202346
