class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = dict()

    def average_grade_lectures(self):
        av_sum_of_grades = 0
        for g in self.grades.values():
            if len(g) > 0:
                av_sum_of_grades += sum(g) / len(g)
            else:
                continue

        if len(self.grades) >0:
            return av_sum_of_grades / len(self.grades)
        else:
            return 'Лектор ещё не был оценён студентами'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade_lectures()}'

class Rewiewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, [])
            student.grades[course].append(grade)
            return None
        else:
            return f'Студент {student.surname} не обучается на курсе {course} или эксперт {self.surname} не курирует данный курс!'



class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Студент:\nИмя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задание: {self.aver_rate_hw()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершённые курсы: {self.finished_courses}')

    def rate_lecturer(self, lecturer, course, grade):
        if course not in self.finished_courses:
            return f'Студент {self.surname} не может оценить курс {course}, потому что не окончил данный курс!'
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, [])
            lecturer.grades[course].append(grade)
            return None
        else:
            return f'Лектор {lecturer.surname} не ведёт курс {course}!'

    def aver_rate_hw(self):
        av_rate = 0
        for v in self.grades.values():
            if len(v) > 0:
                av_rate += sum(v) / len(v)
            else:
                continue
        return av_rate / len(self.grades)



# Создаём ревьюеров
rewiewer1 = Rewiewer('Владимир', 'Володин')
rewiewer1.courses_attached = ['Python', 'PHP', 'Django']
rewiewer2 = Rewiewer('Геннадий', 'Геннадин')
rewiewer2.courses_attached = ['HTML', 'CSS', 'JS']

# print('Ревьюер:\n', rewiewer1, sep='')
# print('Ревьюер:\n', rewiewer2, sep='')

# Создаем лекторов
lecturer1 = Lecturer('Александр', 'Александров')
lecturer1.courses_attached = ['Python', 'PHP', 'Django']
lecturer2 = Lecturer('Борис', 'Борисов')
lecturer2.courses_attached = ['HTML', 'CSS', 'JS', 'PHP']

# print('Лектор:\n', lecturer1, sep='')
# print('Лектор:\n', lecterur2, sep='')

# Создаем студентов
student1 = Student('Олег', 'Олегов', 'м')
student1.courses_in_progress = ['Python', 'PHP', 'JS']
student1.finished_courses = ['HTML', 'Django']
student2 = Student('Елена', 'Еленова', 'ж')
student2.courses_in_progress = ['HTML', 'CSS', 'JS']
student2.finished_courses = ['Python', 'PHP']

# Ревьюеры выставляют оценки студентам
rewiewer1.rate_hw(student1, 'Python', 4)
rewiewer2.rate_hw(student1, 'JS', 5)
rewiewer2.rate_hw(student2, 'HTML', 6)
rewiewer2.rate_hw(student2, 'CSS', 9)

print(student1)
print(student2)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Django', 9)
student1.rate_lecturer(lecturer2, 'HTML', 10)

student2.rate_lecturer(lecturer1, 'Python', 7)
student2.rate_lecturer(lecturer2, 'PHP', 7)

# Средние оценки лекторов за лекции
print(f'Средний бал за лекции, выставленный лектору {lecturer1.surname}: {lecturer1.average_grade_lectures()}')
print(f'Средний бал за лекции, выставленный лектору {lecturer2.surname}: {lecturer2.average_grade_lectures()}')