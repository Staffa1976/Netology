class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = dict()

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_grade_lectures()}')

    def __lt__(self, other):
        return self.average_grade_lectures() < other.average_grade_lectures()

    def __gt__(self, other):
        return self.average_grade_lectures() > other.average_grade_lectures()

    def __eq__(self, other):
        return self.average_grade_lectures() == other.average_grade_lectures()

    def average_grade_lectures(self):
        av_sum_of_grades = 0
        for g in self.grades.values():
            if len(g) > 0:
                av_sum_of_grades += sum(g) / len(g)
            else:
                continue
        if len(self.grades) > 0:
            return av_sum_of_grades / len(self.grades)
        else:
            return 'Лектор ещё не был оценён студентами'


class Rewiewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if grade < 1 or grade > 10:
            return 'Оценка должна быть в диапазоне от 1 до 10!'
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades.setdefault(course, [])
            student.grades[course].append(grade)
            return None
        else:
            return (f'Студент {student.surname} не обучается на курсе {course} или эксперт {self.surname}'
                    f' не курирует данный курс!')


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

    def __lt__(self, other):
        return self.aver_rate_hw() < other.aver_rate_hw()

    def __gt__(self, other):
        return self.aver_rate_hw() > other.aver_rate_hw()

    def __eq__(self, other):
        return self.aver_rate_hw() == other.aver_rate_hw()

    def rate_lecturer(self, lecturer, course, grade):
        if grade < 1 or grade > 10:
            return 'Оценка должна быть в диапазоне от 1 до 10!'
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


def aver_grade_for_students_on_course(list_students, course):
    """Расчёт средней оценки студентов на определённом курсе"""
    aver = 0
    counter = 0
    for st in list_students:
        for cour in st.grades.keys():
            if course == cour:
                aver += sum(st.grades[cour]) / len(st.grades[cour])
                counter += 1
    return aver / counter


def aver_grade_for_lecturers_on_course(list_lecturers, course):
    """Расчёт средней оценки работы лекторов на определённом курсе"""
    aver = 0
    counter = 0
    for lec in list_lecturers:
        for cour in lec.grades.keys():
            if course == cour:
                aver += sum(lec.grades[cour]) / len(lec.grades[cour])
                counter += 1
    return aver / counter


# Создаём ревьюеров
rewiewer1 = Rewiewer('Владимир', 'Володин')
rewiewer1.courses_attached = ['Python', 'PHP', 'Django']
rewiewer2 = Rewiewer('Геннадий', 'Геннадин')
rewiewer2.courses_attached = ['HTML', 'CSS', 'JS']

# # print('Ревьюер:\n', rewiewer1, sep='')
# # print('Ревьюер:\n', rewiewer2, sep='')
#
# Создаем лекторов
lecturer1 = Lecturer('Александр', 'Александров')
lecturer1.courses_attached = ['Python', 'PHP', 'Django']
lecturer2 = Lecturer('Борис', 'Борисов')
lecturer2.courses_attached = ['HTML', 'CSS', 'JS', 'PHP']

list_lecturers = [lecturer1, lecturer2]
#
# # print('Лектор:\n', lecturer1, sep='')
# # print('Лектор:\n', lecterur2, sep='')
#
# Создаем студентов
student1 = Student('Олег', 'Олегов', 'м')
student1.courses_in_progress = ['Python', 'PHP', 'JS']
student1.finished_courses = ['HTML', 'Django']
student2 = Student('Елена', 'Еленова', 'ж')
student2.courses_in_progress = ['HTML', 'CSS', 'JS']
student2.finished_courses = ['Python', 'PHP']
#
list_students = [student1, student2]

# Ревьюеры выставляют оценки студентам
rewiewer1.rate_hw(student1, 'Python', 7)
rewiewer2.rate_hw(student1, 'JS', 8)
rewiewer2.rate_hw(student2, 'HTML', 6)
rewiewer2.rate_hw(student2, 'CSS', 9)

# print(student1)
# print(student2)
#
# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, 'Django', 10)
student1.rate_lecturer(lecturer2, 'HTML', 10)

student2.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'PHP', 7)

# # Средние оценки лекторов за лекции
# print(f'Средний бал за лекции, выставленный лектору {lecturer1.surname}: {lecturer1.average_grade_lectures()}')
# print(f'Средний бал за лекции, выставленный лектору {lecturer2.surname}: {lecturer2.average_grade_lectures()}')
#
# print(lecturer1 < lecturer2)
# print(lecturer1 > lecturer2)
# print(lecturer1 == lecturer2)
#
# print(student1 > student2)

g = aver_grade_for_students_on_course(list_students, 'Python')
print(f'Средняя оценка студентов на курсе "Python" составляет {g}')

g = aver_grade_for_students_on_course(list_lecturers, 'Python')
print(f'Средняя оценка лекторов на курсе "Python" составляет {g}')
