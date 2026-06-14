# Практика 1. Словарь студента
# Создайте словарь student с ключами name,age,group,score. Затем выведите имя, измените балл, добавьте is_active, удалите age и выведите итоговый словарь

# student = {
#     "name": "Ali",
#     "age": 18,
#     "group": "Python-1",
#     "score": 80
# }
# print(student["name"])
# student["score"] = 90
# student["is_active"] = True
# del student["age"]
# print(student)


# Практика 2. Проверка email

# user = {
#     "username": "admin",
#     "password": "12345"
# }

# if "email" in user:
#     print(user["email"])
# else:
#     print("Email не найден")

# print(user.get("email", "Email не найден"))


# Практика 3. Список товаров

# products = [
#     {"title": "Phone", "price": 250000, "count": 3},
#     {"title": "Laptop", "price": 450000, "count": 2},
#     {"title": "Mouse", "price": 8000, "count": 10}
# ]

# for product in products:
#     print(product["title"])
# total = 0
# for product in products:
#     total += product["price"]*product["count"]
# print(total)
# for product in products:
#     if product["price"] > 100000:
#         print(product["title"])


# Практика 4. Частота слов

# words = ["python", "java", "python", "c++", "python", "java"]
# result = {}
# for word in words:
#     result[word] = result.get(word,0) + 1 
# print(result)


# Практика 5. Удаление дубликатов

# numbers = [1,2,2,3,4,4,5,5,5]
# unique_numbers = list(set(numbers))
# print(unique_numbers)

# Практика 6. Общие студенты

# python_students = {"Ali", "Amina", "Dias", "Miras"}
# java_students = {"Amina", "Miras", "Dana", "Sanzhar"}
# both = python_students & java_students
# print(both)

# Практика 7. Только Python

# python_students = {"Ali", "Amina", "Dias", "Miras"}
# java_students = {"Amina", "Miras", "Dana", "Sanzhar"}
# only_python = python_students - java_students
# print(only_python)

# Практика 8. Все студенты без повторений

# python_students = {"Ali", "Amina", "Dias", "Miras"}
# java_students = {"Amina", "Miras", "Dana", "Sanzhar"}
# all_students = python_students|java_students
# print(all_students)


# Комбинация dict + set
# В реальных задачах словари и множества часто используются вместе. Например, словарь хранит студентов, а множество хранит навыки каждого студента.

# students = {
#     "Ali": {"Python", "HTML", "CSS"},
#     "Amina": {"Python", "JavaScript", "React"},
#     "Dias": {"Java", "Spring", "SQL"},
#     "Miras": {"Python", "SQL", "Django"}
# }

# Студенты, которые изучают Python

# for name, courses in students.items():
#     if "Python" in courses:
#         print(name)

# Все уникальные курсы

# all_courses = set()
# for courses in students.values():
#     all_courses.update(courses)
# print(all_courses)

