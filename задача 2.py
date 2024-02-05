"""2.	Напишите функцию make_ice_cream,
 которая принимает один фиксированный аргумент
  flavor (вкус мороженого) и произвольное количество
   дополнительных топпингов (аргументы *toppings).
    Функция должна выводить описание мороженого,
     начиная с вкуса и перечисляя все топпинги."""


def make_ice_cream(flavor, *toppings):
    print(f"Ваше мороженое: {flavor}")

    if toppings:
        print("Топпинги:")
        for topping in toppings:
            print(f"- {topping}")
    else:
        print("Без топпингов")


# Примеры использования
make_ice_cream("Ванильное")
# Вывод: Ваше мороженое: Ванильное
#        Без топпингов

make_ice_cream("Шоколадное", "Орехи", "Шоколадный соус", "Вишня")
# Вывод: Ваше мороженое: Шоколадное
#        Топпинги:
#        - Орехи
#        - Шоколадный соус
#        - Вишня

make_ice_cream("Пломбир","Малина")