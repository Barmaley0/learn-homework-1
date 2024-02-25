"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

IPHONE_12 = 0
XIAOMI_MI11 = 1
SAMSUNG_GALAXY_21 = 2

def main():
    phones = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358,
                                                480, 476, 470, 216,
                                                270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431,
                                                  211, 354, 276, 526,
                                                  141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437,
                                                        214, 494, 441, 518,
                                                        212, 288, 272, 247]}
    ]

    iphone_12 = total_quantity_sale_product(phones, IPHONE_12)
    xiaomi_mi11 = total_quantity_sale_product(phones, XIAOMI_MI11)
    samsung_galaxy_21 = total_quantity_sale_product(phones, SAMSUNG_GALAXY_21)

    average_quantity_sale_product(phones, IPHONE_12)
    average_quantity_sale_product(phones, XIAOMI_MI11)
    average_quantity_sale_product(phones, SAMSUNG_GALAXY_21)

    total_sale_product = iphone_12 + xiaomi_mi11 + samsung_galaxy_21
    print(f"Суммарное количество продаж всех товаров составит - {total_sale_product} шт.")
    total_average_product = total_sale_product / (len(phones[IPHONE_12]["items_sold"]) +
                                                  len(phones[XIAOMI_MI11]["items_sold"]) +
                                                  len(phones[SAMSUNG_GALAXY_21]["items_sold"]))
    print(f"Среднее количество продаж всех товаров составит - {total_average_product:.0f} шт.")

def total_quantity_sale_product(phones, name_product):
    total_sum = 0
    for price in phones[name_product]["items_sold"]:
        total_sum += price
    print(f"Сумма количества продаж {phones[name_product]['product']} "
        f"- {total_sum:,.0f} шт.")
    return total_sum

def average_quantity_sale_product(phones, name_product):
    total_sum = 0
    for price in phones[name_product]["items_sold"]:
        total_sum += price
    average_sale = total_sum / len(phones[name_product]["items_sold"])
    print(f"Среднее количество продаж для {phones[name_product]['product']} "
        f"- {average_sale:,.0f} шт.")

if __name__ == "__main__":
    main()
