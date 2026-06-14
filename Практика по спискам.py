# Практика по спискам.
# Практика 1. Список студентов
# Создайте список из 5 студентов. Выведите первого, последнего, добавьте нового студента, удалите одного студента, отсортируйте список и выведите всех студентов через цикл.

# students = ["Arman", "Anna", "Zhanna", "Sultan", "Elena"]
# print("Первый студент:", students[0])
# print("Последний студент:", students[-1])
# students.append("Vera")
# students.remove ("Zhanna")
# students.sort()
# print("\nСписок студентов:")
# for student in students:
#     print(student)

# Практика 2. Оценки
# Дан список grades = [5, 4, 3, 5, 2, 4, 5]. Найти количество оценок, сумму, среднюю оценку, максимум, минимум и количество пятерок.

# grades = [5, 4, 3, 5, 2, 4, 5]
# count = len(grades)
# total = sum(grades)
# average = total/count
# maximum = max(grades)
# minimum = min(grades)
# fives = grades.count(5)
# print("Количество оценок:", count)
# print("Сумма оценок:", total)
# print("Средняя оценка:", average)
# print("Максимальная оценка:", maximum)
# print("Минимальная оценка:", minimum)
# print("Количество пятерок:", fives)

# Практика 3. Фильтр чисел
# Дан список numbers = [10, -5, 3, -2, 0, 8, -1]. Создайте positive_numbers и negative_numbers. Разложите числа по спискам.

# numbers = [10, -5, 3, -2, 0, 8, -1]
# positive_numbers = []
# negative_numbers = []
# for number in numbers:
#     if number > 0:
#         positive_numbers.append(number)
#     elif number < 0:
#         negative_numbers.append(number)
# print("Положительные числа:", positive_numbers)
# print("Отрицательные числа:", negative_numbers)

# Практика 4. Корзина
# Создайте пустой список cart. Добавьте товары, удалите один товар, проверьте наличие товара, очистите корзину.

cart = []
cart.append("яблоко")
cart.append("хлеб")
cart.append("молоко")
cart.append("сыр")
print("Корзина после добавления:", cart)
cart.remove("хлеб")
print("После удаления:", cart)
if "молоко" in cart:
    print("Молоко есть в корзине")
else:
    print("Молока нет в корзине")
cart.clear()
print("Корзина после очистки:", cart)

