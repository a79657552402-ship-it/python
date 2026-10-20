# Задание 3: Словари и множества
# Напишите программу, которая:
# 1. Создает словарь с информацией о студентах (имя, возраст, оценки)
# 2. Находит всех студентов с оценкой выше 4
# 3. Создает множество уникальных оценок
# 4. Демонстрирует разницу между списком и множеством при поиске элементов

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def insert_data(self):
        dct = {self.name: [self.age, self.grade]}
        return (dct)

    def __str__(self):
        return f'{self.insert_data()}'


class Journal:
    def __init__(self):
        self.record = {}

    def add_student(self, student):
        self.record[student.name] = [student.age, student.grade]

    def __str__(self):
        return f'{self.record}'


class FindStudent:
    def __init__(self):
        self.names = []

    def find_grade(self, journal):
        self.names = []
        for name, (age, grades) in journal.record.items():
            if grades > 4:
                self.names.append(name)
                return self.names
    def __str__(self):
        return self.names


j = Journal()
j.add_student(Student('Masha', 18, [5, 5, 5, 5]))
j.add_student(Student('Kate', 18, [5, 5, 5, 5]))
j.add_student(Student('Dasha', 19, [3, 4, 5, 3]))
j.add_student(Student('Sasha', 20, [5, 4, 5, 3]))
hash(j)
f = FindStudent()
f.find_grade(j)
print(f)
