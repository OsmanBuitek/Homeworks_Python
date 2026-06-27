# Домашнее задание 1. Анкета пользователя
# Создайте словарь user, где будут ключи name, age, email, city, skills. Ключ skills должен хранить множество.

# user = {
#     "name": "Ali",
#     "age": 18,
#     "email": "ali@mail.com",
#     "city": "Almaty",
#     "skills": {"Python", "HTML", "CSS"}
# }

# # Вывести имя и город пользователя
# print("Имя:", user["name"])
# print("Город:", user["city"])

# # Добавить новый навык
# user["skills"].add("Django")
# print("После добавления навыка:", user["skills"])

# # Удалить один навык
# user["skills"].remove("CSS")
# print("После удаления навыка:", user["skills"])

# # Проверить, знает ли пользователь Python
# if "Python" in user["skills"]:
#     print("Пользователь знает Python")
# else:
#     print("Пользователь не знает Python")

# # Вывести все ключи словаря
# print("Ключи:", user.keys())

# # Вывести все значения словаря
# print("Значения:", user.values())


# Домашнее задание 2. Система товаров

# products = [
#     {"title": "Phone", "price": 250000, "category": "tech", "count": 3},
#     {"title": "Laptop", "price": 450000, "category": "tech", "count": 2},
#     {"title": "Bread", "price": 300, "category": "food", "count": 10},
#     {"title": "Milk", "price": 500, "category": "food", "count": 5}
# ]

# # Вывести все товары
# print("Все товары:")
# for product in products:
#     print(product)

# # Найти товары дороже 100000
# print("\nТовары дороже 100000:")
# for product in products:
#     if product["price"] > 100000:
#         print(product)

# # Посчитать общую стоимость склада с учетом count
# total = 0
# for product in products:
#     total += product["price"]*product["count"]
# print("\nОбщая стоимость склада:", total)

# # Найти все уникальные категории
# categories = set()
# for product in products:
#     categories.add(product["category"])
# print("\nУникальные категории:", categories)

# # Найти количество товаров категории food
# food_count = 0
# for product in products:
#     if product["category"] == "food":
#         food_count += 1
# print("\nКоличество товаров категории food:", food_count)

# # Найти количество товаров категории tech
# tech_count = 0
# for product in products:
#     if product["category"] == "tech":
#         tech_count += 1
# print("\nКоличество товаров категории tech:", tech_count)

# # Найти общее количество единиц на складе категории food 
# food_count = 0
# for product in products:
#     if product["category"] == "food":
#         food_count += product["count"]
# print("\nОбщее количество единиц на складе категории food:", food_count)

# # Найти общее количество единиц на складе категории tech
# tech_count = 0
# for product in products:
#     if product["category"] == "tech":
#         tech_count += product["count"]
# print("\nОбщее количество единиц на складе категории tech:", tech_count)

# Домашнее задание 3. Студенты и оценки

# students = [
#     {"name": "Ali", "scores": [80, 90, 70], "skills": {"Python", "HTML"}},
#     {"name": "Amina", "scores": [95, 88, 92], "skills": {"Python", "React"}},
#     {"name": "Dias", "scores": [60, 75, 70], "skills": {"Java", "SQL"}}
# ]

# # Вывести имя каждого студента
# print("Имена студентов:")
# for student in students:
#     print(student["name"])

# # Посчитать средний балл каждого студента.
# print("\nСредний балл каждого студента:")
# for student in students:
#     avg = sum(student["scores"])/len(student["scores"])
#     print(student["name"], ":", avg)

# # Найти студентов, которые знают Python
# print("\nСтуденты, которые знают Python:")
# for student in students:
#     if "Python" in student["skills"]:
#         print(student["name"])


# # Собрать все уникальные навыки
# print("\nВсе уникальные навыки студентов:")
# all_skills = set()
# for student in students:
#     all_skills.update(student["skills"])
# print(all_skills)

# # Найти студента с самым высоким средним баллом.
# print("\nСтудент с самым высоким средним баллом:")
# best_student = ""
# best_avg = 0
# for student in students:
#     avg = sum(student["scores"])/len(student["scores"])

#     if avg > best_avg:
#         best_avg = avg
#         best_student = student["name"]
# print("Лучший студент:", best_student)
# print("Средний балл:", best_avg)


# Домашнее задание 4. Частота слов
# text = "apple banana apple orange banana apple"
# Нужно получить словарь частоты слов:

# text = "apple banana apple orange banana apple"
# words = text.split()
# freq = {}
# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1
# print(freq)











