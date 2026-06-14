# Задача 1. Проверка числа
# number = int(input("Введите число: "))
# if number > 0:
#     print ("Положительное")
# elif number < 0:
#     print ("Отрицательное")
# elif number == 0:
#     print ("Ноль")
# else:
#     print ("Другое")


# Задача 2. Четное или нечетное
# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print ("Четное")
# elif number % 2 == 1:
#     print ("Нечетное")


# Задача 3. Возрастная категория
# age = int(input("Введите возраст: "))
# if age < 7:
#     print("Ребенок")
# elif age <= 17:
#     print("Школьник")
# elif age <= 59:
#     print("Взрослый")
# else:
#     print("Пенсионер")


# Задача 4. Оценка по баллам
# score = int(input("Введите баллы от 0 до 100: "))
# if 90 <= score <= 100:
#     print("Отлично")
# elif 75 <= score <= 89:
#     print("Хорошо")
# elif 50 <= score <= 74:
#     print("Сдал")
# elif score < 0 or score > 100:
#     print ("Некорректный балл")
# else:
#     print ("Не сдал")

# Задача 5. Проверка пароля через not
# password = input("Введите пароль: ")
# if not (password == "admin"):
#     print("Ошибка")
# else:
#     print("Верно")

# Задача 6. Доступ в кино
# age = int(input("Введите возраст: "))
# adult = input("Есть ли взрослый сопровождающий? (да/нет): ")
# if age >= 16 or adult == "да":
#     print("Можно на фильм")
# else:
#     print("Нельзя")

# Задача 7. Скидка в магазине
# age = int(input("Введите возраст: "))
# student = input("Вы студент? (да/нет): ")
# if age < 18 or student == "да":
#     print("Скидка 30%")
# elif age >= 18 and student == "нет":
#     print("Скидки нет")

# Задача 8. Погода и одежда
# temp = int(input("Введите температуру: "))
# wind = input("Сильный ли ветер? (да/нет): ")
# if temp < 0 or wind == "да":
#     print("Нужна теплая одежда")
# elif 0 < temp < 15:
#     print("Куртка")
# elif temp > 15:
#     print("Легкая одежда")

# Задача 9. Авторизация с разными ошибками
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# if login == "admin" and password == "12345":
#     print("Вход выполнен")
# elif login == "admin" and not (password == "12345"):
#     print("Неправильный пароль")
# else:
#     print("Пользователь не найден")

# Задача 10. Банковская операция с вложенными условиями
# age = int(input("Введите возраст: "))
# balance = int(input("Введите баланс карты: "))
# status = input("Заблокирована ли карта? (да/нет): ")
# if age < 18:
#     print("Операция доступна только с 18 лет")
# elif age >= 18 and balance < 1000:
#     print("Недостаточно средств")
# elif age >= 18 and balance >= 1000 and status == ("да"):
#     print("Карта заблокирована")
# else:
#     print("Операция разрешена")


