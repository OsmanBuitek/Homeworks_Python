# Часть 2. Доработать проект "Журнал студентов"
# 74.Добавить создание нового студента.
# 75.Добавить удаление студента.
# 76.Добавить поиск студентов по группе.
# 77.Добавить метод is_passed, который возвращает True, если средний балл >= 50.
# 78.Добавить метод get_status, который возвращает "Отличник", "Хорошист" или "Нужно
# подтянуться".
# 79.Сделать проверку ввода возраста и оценки.
# 80.Разделить проект на файлы: main.py, student.py, utils.py.

from student import Student
from utils import add_student, delete_student, search_by_group, input_student

# Начальные данные
students = [
    Student("Алия Сейткали",      19, "ИС-21", [90, 85, 88, 92]),
    Student("Данияр Ахметов",     20, "ИС-21", [60, 55, 70, 65]),
    Student("Жанна Нурланова",    18, "ИТ-22", [40, 35, 50, 45]),
    Student("Марат Джаксыбеков", 21, "ИТ-22", [75, 80, 70, 85]),
    Student("Айгерим Касымова",   19, "ИС-21", [95, 98, 100, 92]),
]


def show_students(lst=None):
    if lst is None:
        lst = students
    if not lst:
        print("Студенты не найдены.")
        return
    print()
    for i, s in enumerate(lst, 1):
        print(f"{i}. {s}")


def main():
    while True:
        print("\n====== ЖУРНАЛ СТУДЕНТОВ ======")
        print("1. Показать всех студентов")
        print("2. Добавить студента")
        print("3. Удалить студента")
        print("4. Поиск по группе")
        print("0. Выход")

        choice = input("\nВыберите действие: ").strip()

        if choice == "1":
            show_students()

        elif choice == "2":
            s = input_student()
            add_student(students, s)

        elif choice == "3":
            name = input("Введите имя студента для удаления: ").strip()
            delete_student(students, name)

        elif choice == "4":
            group = input("Введите название группы: ").strip()
            found = search_by_group(students, group)
            show_students(found)

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
