# Часть 1. Доработать проект "Кафе"
# 65.Добавить минимум 10 блюд.
# 66.Добавить минимум 4 категории.
# 67.Сделать поиск блюда по названию.
# 68.Сделать фильтр по категории.
# 69.Сделать удаление блюда из заказа.
# 70.Сделать изменение количества.
# 71.Добавить скидку от 10000 тг.
# 72.Добавить историю заказов.
# 73.Сделать проверку, что нельзя заказать больше 10 одинаковых блюд.

# ============ Проект "Кафе" ============

menu = [
    {"id": 1,  "name": "Плов",          "category": "Горячее",  "price": 1500},
    {"id": 2,  "name": "Манты",         "category": "Горячее",  "price": 1200},
    {"id": 3,  "name": "Шашлык",        "category": "Горячее",  "price": 2000},
    {"id": 4,  "name": "Лагман",        "category": "Супы",     "price": 1000},
    {"id": 5,  "name": "Борщ",          "category": "Супы",     "price": 900},
    {"id": 6,  "name": "Самса",         "category": "Выпечка",  "price": 300},
    {"id": 7,  "name": "Баурсак",       "category": "Выпечка",  "price": 200},
    {"id": 8,  "name": "Чай",           "category": "Напитки",  "price": 150},
    {"id": 9,  "name": "Кофе",          "category": "Напитки",  "price": 350},
    {"id": 10, "name": "Айран",         "category": "Напитки",  "price": 200},
    {"id": 11, "name": "Салат Цезарь",  "category": "Салаты",   "price": 800},
    {"id": 12, "name": "Оливье",        "category": "Салаты",   "price": 700},
]

order = []          
order_history = []  


def show_menu(dishes=None):
    if dishes is None:
        dishes = menu
    if not dishes:
        print("Блюда не найдены.")
        return
    print(f"\n{'ID':<5} {'Название':<20} {'Категория':<12} {'Цена (тг)'}")
    print("-" * 52)
    for d in dishes:
        print(f"{d['id']:<5} {d['name']:<20} {d['category']:<12} {d['price']}")


def search_by_name(name):
    """Поиск блюда по названию."""
    return [d for d in menu if name.lower() in d["name"].lower()]


def filter_by_category(category):
    """Фильтр по категории."""
    return [d for d in menu if d["category"].lower() == category.lower()]


def add_to_order(dish_id, quantity=1):
    dish = next((d for d in menu if d["id"] == dish_id), None)
    if not dish:
        print("Блюдо не найдено.")
        return
    for item in order:
        if item["dish"]["id"] == dish_id:
            # Проверка: нельзя больше 10 
            if item["quantity"] + quantity > 10:
                print("Нельзя заказать больше 10 одинаковых блюд!")
                return
            item["quantity"] += quantity
            print(f"'{dish['name']}' — количество обновлено: {item['quantity']} шт.")
            return
    if quantity > 10:
        print("Нельзя заказать больше 10 одинаковых блюд!")
        return
    order.append({"dish": dish, "quantity": quantity})
    print(f"'{dish['name']}' добавлено в заказ.")


def remove_from_order(dish_id):
    """Удаление блюда из заказа."""
    for item in order:
        if item["dish"]["id"] == dish_id:
            order.remove(item)
            print(f"'{item['dish']['name']}' удалено из заказа.")
            return
    print("Блюдо не найдено в заказе.")


def change_quantity(dish_id, quantity):
    """Изменение количества."""
    if quantity < 1 or quantity > 10:
        print("Количество должно быть от 1 до 10.")
        return
    for item in order:
        if item["dish"]["id"] == dish_id:
            item["quantity"] = quantity
            print(f"Количество '{item['dish']['name']}' изменено на {quantity}.")
            return
    print("Блюдо не найдено в заказе.")


def show_order():
    if not order:
        print("Заказ пуст.")
        return
    total = 0
    print(f"\n{'Название':<20} {'Кол-во':<8} {'Цена':<10} {'Сумма'}")
    print("-" * 50)
    for item in order:
        subtotal = item["dish"]["price"] * item["quantity"]
        total += subtotal
        print(f"{item['dish']['name']:<20} {item['quantity']:<8} {item['dish']['price']:<10} {subtotal}")
    # Скидка от 10000 тг 
    if total >= 10000:
        discount = total * 0.10
        print(f"\nСкидка 10% (заказ от 10 000 тг): -{discount:.0f} тг")
        print(f"Итого со скидкой: {total - discount:.0f} тг")
    else:
        print(f"\nИтого: {total} тг")
        print(f"(До скидки не хватает: {10000 - total} тг)")


def place_order():
    """Оформить заказ и добавить в историю."""
    if not order:
        print("Заказ пуст.")
        return
    total = sum(i["dish"]["price"] * i["quantity"] for i in order)
    discount = total * 0.10 if total >= 10000 else 0
    final = total - discount
    order_history.append({
        "items": [
            {"name": i["dish"]["name"], "qty": i["quantity"], "price": i["dish"]["price"]}
            for i in order
        ],
        "total": final,
    })
    print(f"\nЗаказ #{len(order_history)} оформлен! К оплате: {final:.0f} тг")
    order.clear()


def show_history():
    """История заказов."""
    if not order_history:
        print("История заказов пуста.")
        return
    for i, o in enumerate(order_history, 1):
        print(f"\n--- Заказ #{i} ---")
        for item in o["items"]:
            print(f"  {item['name']} x{item['qty']} = {item['price'] * item['qty']} тг")
        print(f"  Итого: {o['total']:.0f} тг")


def main():
    while True:
        print("\n========== КАФЕ ==========")
        print("1. Показать меню")
        print("2. Поиск блюда по названию")
        print("3. Фильтр по категории")
        print("4. Добавить блюдо в заказ")
        print("5. Удалить блюдо из заказа")
        print("6. Изменить количество")
        print("7. Показать текущий заказ")
        print("8. Оформить заказ")
        print("9. История заказов")
        print("0. Выход")

        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            show_menu()

        elif choice == "2":
            name = input("Введите название блюда: ").strip()
            show_menu(search_by_name(name))

        elif choice == "3":
            print("Доступные категории: Горячее, Супы, Выпечка, Напитки, Салаты")
            cat = input("Введите категорию: ").strip()
            show_menu(filter_by_category(cat))

        elif choice == "4":
            show_menu()
            try:
                dish_id = int(input("Введите ID блюда: "))
                qty = int(input("Количество: "))
                add_to_order(dish_id, qty)
            except ValueError:
                print("Ошибка: введите числовое значение.")

        elif choice == "5":
            show_order()
            try:
                dish_id = int(input("Введите ID блюда для удаления: "))
                remove_from_order(dish_id)
            except ValueError:
                print("Ошибка: введите числовое значение.")

        elif choice == "6":
            show_order()
            try:
                dish_id = int(input("Введите ID блюда: "))
                qty = int(input("Новое количество (1-10): "))
                change_quantity(dish_id, qty)
            except ValueError:
                print("Ошибка: введите числовое значение.")

        elif choice == "7":
            show_order()

        elif choice == "8":
            place_order()

        elif choice == "9":
            show_history()

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
