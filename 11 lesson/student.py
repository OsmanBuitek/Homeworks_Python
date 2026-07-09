class Student:
    def __init__(self, name, age, group, grades):
        self.name = name
        self.age = age
        self.group = group
        self.grades = grades  

    def average(self):
        """Средний балл"""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def is_passed(self):
        """Возвращает True, если средний балл >= 50"""
        return self.average() >= 50

    def get_status(self):
        """Возвращает статус студента"""
        avg = self.average()
        if avg >= 85:
            return "Отличник"
        elif avg >= 65:
            return "Хорошист"
        else:
            return "Нужно подтянуться"

    def __str__(self):
        passed = "✓ Сдал" if self.is_passed() else "✗ Не сдал"
        return (
            f"{self.name:<20} | Группа: {self.group:<8} | "
            f"Возраст: {self.age:<3} | Средний балл: {self.average():<6.1f} | "
            f"{self.get_status()} | {passed}"
        )
