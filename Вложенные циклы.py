# Задача: Фильтрация и сортировка списка книг
# Условие
# Создать список книг. Вывести книги, начинающиеся на буквы А или Б. Отсортировать отфильтрованный список по алфавиту без использования sort(). Вывести результат.

# books = ["Белый Клык", 
#          "Автостопом по галактике",
#            "Над пропастью во ржи", 
#            "Братья Карамазовы", 
#            "Бойцовский клуб", 
#            "Алиса в стране чудес",
#            "Три товарища",
#            "Гордость и предубеждение",
#            "Бегущий за ветром",
#            "Маленький принц",
#            "Белая гвардия",
#            "Алхимик",
#            "Ася"]
# filtered_books = []
# for book in books:
#     if book.startswith("А") or book.startswith("Б"):
#         filtered_books.append(book)
# n = len(filtered_books)
# for i in range(n):
#     for j in range(0, n - i - 1):
#         if filtered_books [j] > filtered_books[j + 1]:
#             filtered_books[j], filtered_books[j + 1] = (filtered_books[j + 1], filtered_books[j])
# print("Отфильтрованный и отсортированный список:")
# for book in filtered_books:
#     print(book)
