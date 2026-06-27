# 13.1. Простые функции

# # 1. Создать функцию get_square(number), которая возвращает квадрат числа
# def get_square(number):
#     return number ** 2

# # 2. Создать функцию is_negative(number), которая возвращает True, если число отрицательное
# def is_negative(number):
#     return number < 0

# # 3. Создать функцию format_name(name), которая убирает пробелы и делает первую букву заглавной
# def format_name(name):
#     return name.strip().capitalize()

# # 4. Создать функцию get_last_item(items), которая возвращает последний элемент списка
# def get_last_item(items):
#     return items[-1]

# 5. Создать функцию count_words(text), которая возвращает количество слов в строке
# def count_words(text):
#     return len(text.split())

# Тестовые вызовы функций
# print("1.", get_square(8))
# print("2.", is_negative(-15))
# print("3.", format_name("    Кабинет    "))
# print("4.", get_last_item([13, 24, 45, 78]))
# print("5.", count_words("Добро пожаловать в город!"))


# # 13.2. Функции со списками

# # 6. Создать функцию get_even_numbers(numbers), которая возвращает только четные числа
# def get_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]

# # 7. Создать функцию get_long_words(words), которая возвращает слова длиннее 5 символов
# def get_long_words(words):
#     return [word for word in words if len(word) > 5]

# # 8. Создать функцию get_average_grade(grades), которая возвращает среднюю оценку
# def get_average_grade(grades):
#     return sum(grades) / len(grades)

# # 9. Создать функцию has_failed_grade(grades), которая возвращает True, если есть оценка меньше 50
# def has_failed_grade(grades):
#     return any(grade < 50 for grade in grades)

# # 10.Создать функцию normalize_numbers(numbers), которая возвращает новый список, где каждое число делится на максимальное число списка
# def normalize_numbers(numbers):
#     max_num = max(numbers)
#     return [num / max_num for num in numbers]

# # Тестовые вызовы функций
# print("6.", get_even_numbers([13, 34, 45, 56, 77, 88, 91, 96]))
# print("7.", get_long_words(["погода", "стол", "лампа", "солнце", "дверь", "благополучие", "код", "мышь"]))
# print("8.", get_average_grade([76, 75, 81, 90, 70]))
# print("9.", has_failed_grade([95, 42, 57, 81, 77]))
# print("10.", normalize_numbers([4, 8, 10, 16, 20]))


# # 13.3. Функции со словарями

# # 11.Создать функцию create_product(title, price, category), которая возвращает словарь товара
# def create_product(title, price, category):
#     return {
#         "title": title,
#         "price": price,
#         "category": category
#     }

# # 12.Создать функцию apply_discount(product, discount), которая возвращает цену товара со скидкой
# def apply_discount(product, discount):
#     return product["price"] * (1 - discount / 100)

# # 13.Создать функцию get_user_info(user), которая возвращает строку вида: Имя: Ayan, Возраст: 18
# def get_user_info(user):
#     return f"Имя: {user['name']}, Возраст: {user['age']}"

# # 14.Создать функцию add_skill(user, skill), которая добавляет навык пользователю в множество skills
# def add_skill(user, skill):
#     user["skills"].add(skill)
#     return user

# # 15.Создать функцию is_admin(user), которая проверяет, равна ли роль пользователя admin
# def is_admin(user):
#     return user["role"] == "admin"

# # Тестовые вызовы функций
# product = create_product("Iphone 17 Pro", 900000, "Electronics")
# print("11.", product)

# print("12.", apply_discount(product, 30))

# user = {
#     "name": "Ayan",
#     "age": 18,
#     "skills": {"HTML"},
#     "role": "admin"
# }

# print("13.", get_user_info(user))

# print("14.", add_skill(user, "CSS"))

# print("15.", is_admin(user))


# 13.4. Большая задача - мини-анализ интернет-магазина

# Даны товары:

# products = [
#  {"title": "Laptop", "price": 350000, "category": "Electronics", "rating": 4.8},
#  {"title": "Mouse", "price": 8000, "category": "Electronics", "rating": 4.4},
#  {"title": "Book", "price": 5000, "category": "Education", "rating": 4.9},
#  {"title": "Pen", "price": 500, "category": "Education", "rating": 4.1},
#  {"title": "Desk", "price": 45000, "category": "Furniture", "rating": 4.6}
# ]

# # Нужно написать функции:
# # 1. get_total_price(products) - возвращает сумму всех товаров;
# # 2. get_products_by_category(products, category) - возвращает товары указанной категории;
# # 3. get_expensive_products(products, min_price) - возвращает товары дороже указанной цены;
# # 4. get_best_product(products) - возвращает товар с самым высоким рейтингом;
# # 5. show_products_report(products) - выводит красивый отчет по товарам.

# # 1. Сумма всех товаров
# def get_total_price(products):
#     total = 0
#     for product in products:
#         total += product["price"]
#     return total

# # 2. Товары указанной категории
# def get_products_by_category(products, category):
#     result = []
#     for product in products:
#         if product["category"] == category:
#             result.append(product)
#     return result

# # 3. Товары дороже указанной цены
# def get_expensive_products(products, min_price):
#     result = []
#     for product in products:
#         if product["price"] > min_price:
#             result.append(product)
#     return result

# # 4. Товар с самым высоким рейтингом
# def get_best_product(products):
#     best = products[0]
#     for product in products:
#         if product["rating"] > best["rating"]:
#             best = product
#     return best

# # 5. Красивый отчет 
# def show_products_report(products):
#     print("Отчет по товарам:")
#     for product in products:
#         print(
#             f"{product['title']} | "
#             f"Цена: {product['price']} | "
#             f"Категория: {product['category']} | "
#             f"Рейтинг: {product['rating']}"
#         )

# # Тестовые вызовы
# print("Общая стоимость:", get_total_price(products))

# print("\nТовары категории Electronics:")
# print(get_products_by_category(products, "Electronics"))

# print("\nТовары дороже 10000:")
# print(get_expensive_products(products, 10000))

# print("\nЛучший товар:")
# print(get_best_product(products))

# print("\nОтчет:")
# show_products_report(products)

