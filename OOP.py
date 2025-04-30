class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}


class Rewiewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, [])
            student.grades[course].append(grade)
            return None
        else:
            print(f'Студент {student.surname} не обучается на курсе {course} '
                  f'или эксперт {self.surname} не курирует данный курс!')
            return None


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if course not in self.finished_courses:
            print(f'Студент {self.surname} не может оценить курс {course}, потому что не окончил данный курс!')
            return None
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, [])
            lecturer.grades[course].append(grade)
        else:
            print(f'Лектор {lecturer.surname} не ведёт курс {course}!')
        return None


# Список лекторов и что преподают
lecturer1 = Lecturer('Александр', 'Александров')
lecturer1.courses_attached = ['Python', 'PHP']

lecturer2 = Lecturer('Борис', 'Борисов')
lecturer2.courses_attached = ['JS', 'HTML']

# Создание ревьюеров
rewiewer1 = Rewiewer('Владимир', 'Володин')
rewiewer1.courses_attached = ['Python', 'PHP', 'JS', 'HTML']

# Проверка получившегося
print(f'Лектор {lecturer1.name} {lecturer1.surname} ведёт следующие курсы: {lecturer1.courses_attached}.')
print(f'Лектор {lecturer2.name} {lecturer2.surname} ведёт следующие курсы: {lecturer2.courses_attached}.')
print()

# Список студентов и что изучают
student1 = Student('Иван', 'Иванов', 'м')
student1.finished_courses = ["Python", 'JS', 'HTML']
student1.courses_in_progress = ['JS']

student2 = Student('Пётр', 'Петров', 'м')
student2.finished_courses = ["Python", 'С++', 'PHP']
student2.courses_in_progress = ['HTML']

# Проверка получившегося
print(f'Студент {student1.surname} {student1.name} закончил следующие курсы: {student1.finished_courses}.')
print(f'Студент {student2.surname} {student2.name} закончил следующие курсы: {student2.finished_courses}.')
print()

# Оценки лекторов студентами
student1.rate_lecturer(lecturer1, 'Python', 5)
student2.rate_lecturer(lecturer2, 'HTML', 3)
student1.rate_lecturer(lecturer1, 'JS', 4)
student2.rate_lecturer(lecturer1, 'Python', 4)

# Проверка получившегося
print(
    f'Лектор {lecturer1.name} {lecturer1.surname} получил следующую оценку своих усилий от студентов: {lecturer1.grades}.')
print()

# Оценка студентов ревьюерами
rewiewer1.rate_hw(student1, 'JS', 3)
rewiewer1.rate_hw(student2, 'HTML', 4)

# Проверка получившегося
print(f'Студент {student1.surname} имеет следующие оценки {student1.grades}.')
print(f'Студент {student2.surname} имеет следующие оценки {student2.grades}.')
