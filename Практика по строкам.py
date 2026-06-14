# Практика 1. Очистка имени
# Пользователь вводит имя. Уберите пробелы по краям, сделайте первую букву большой и выведите приветствие.

# name = input("Введите имя:")
# clean_name = name.strip().capitalize()
# print(f"Привет,{clean_name}!")

# Практика 2. Проверка email
# Пользователь вводит email. Проверьте, есть ли @ и заканчивается ли email на .com.

# email = input("Введите email:")
# if "@" in email and email.endswith(".com"):
#     print("email корректный")
# else: 
#     print("email некорректный")

# Практика 3. Подсчет слов
# Пользователь вводит предложение.Посчитайте количество слов через split() и len()

# text = input("Введите предложение:")
# words = text.split()
# count = len(words)
# print("Количество слов:", count)

# Практика 4. Поиск плохих слов
# Есть список bad_words. Нужно проверить, встречаются ли эти слова в тексте пользователя.

# bad_words = ["bad","spam","hack"]
# text = input("Введите текст:").lower()
# found = False
# for word in bad_words:
#     if word in text:
#         found = True
#         print("Найдено запрещенное слово:",word)
# if not found:
#     print("Запрещенных слов не найдено")

