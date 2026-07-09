
from student import Student


def validate_age(age):
    """Проверка ввода возраста"""
    if not isinstance(age, int) or age < 14 or age > 100:
        raise ValueError("Возраст должен быть целым числом от 14 до 100.")
    return True


def validate_grade(grade):
    """Проверка ввода оценки"""
    if not isinstance(grade, int) or grade < 0 or grade > 100:
        raise ValueError("Оценка должна быть целым числом от 0 до 100.")
    return True


def add_student(students, student):
    """Добавить нового студента"""
    students.append(student)
    print(f"Студент '{student.name}' успешно добавлен.")


def delete_student(students, name):
    """Удалить студента по имени"""
    for s in students:
        if s.name.lower() == name.lower():
            students.remove(s)
            print(f"Студент '{s.name}' удалён.")
            return
    print(f"Студент '{name}' не найден.")


def search_by_group(students, group):
    """Поиск студентов по группе"""
    return [s for s in students if s.group.lower() == group.lower()]


def input_student():
    """Ввод данных нового студента с валидацией."""
    name = input("Имя студента: ").strip()

    while True:
        try:
            age = int(input("Возраст: "))
            validate_age(age)
            break
        except ValueError as e:
            print(f"Ошибка: {e}")

    group = input("Группа: ").strip()

    grades = []
    print("Введите оценки (0–100), пустая строка — завершить ввод:")
    while True:
        inp = input("  Оценка: ").strip()
        if inp == "":
            break
        try:
            g = int(inp)
            validate_grade(g)
            grades.append(g)
        except ValueError as e:
            print(f"  Ошибка: {e}")

    return Student(name, age, group, grades)
