class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _Average_rating(self):
        try:
            count, c_len = 0, 0
            for i in self.grades: 
                count += sum(self.grades[i])
                c_len += len(self.grades[i])
            return count/c_len
        except ZeroDivisionError:
            return 0
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._Average_rating()}\nКурсы в процессе изучения: {", ".join([i for i in self.courses_in_progress])}\nЗавершенные курсы: {", ".join([i for i in self.finished_courses])}'

    def rate_Lecture(self, lecture, course, grade): # Выставление оценок студентами лекторам
        if isinstance(lecture, Lecture) and course in self.courses_in_progress and course in lecture.courses_attached:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __lt__(self, other):
        return self._Average_rating() < other._Average_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        

        
class Lecture(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _Average_rating(self):
        try:
            count, c_len = 0, 0
            for i in self.grades: 
                count += sum(self.grades[i])
                c_len += len(self.grades[i])
            return count/c_len
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._Average_rating()}'

    def __lt__(self, other):
        return self._Average_rating() < other._Average_rating()

class Rewiwer(Mentor):  
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade): # Выставление оценок экспертами студентам 
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def average_rating_students(students :list, theme :str):
    count, c_len = 0, 0
    for i in students:
         if i.grades.get(theme):
            count += sum(i.grades.get(theme))
            c_len += len(i.grades.get(theme))
    print(f'В рамках курса {theme} средняя оценка за Д/З всех студентов равна {count/c_len}')
        

def average_rating_lectures(lectures :list, theme :str):
    count, c_len = 0, 0
    for i in lectures:
        if i.grades.get(theme):
            count += sum(i.grades.get(theme))
            c_len += len(i.grades.get(theme))
    print(f'В рамках курса {theme} средняя оценка за лекции всех лекторов равна {count/c_len}')


def main():
    best_student1 = Student('Student', 'One', 'M')
    best_student1.courses_in_progress += ['Python', 'SQL', 'HTML', 'CSS']
    best_student1.finished_courses += ['How to be cool', 'Ruby']

    best_student2 = Student('Student', 'Two', 'M')
    best_student2.courses_in_progress += ['C++', 'Python', 'SQL']
    best_student2.finished_courses += ['Drive']
    
    cool_lecture1 = Lecture('Lecture', 'One')
    cool_lecture1.courses_attached += ['Python']

    cool_lecture2 = Lecture('Lecture', 'Two')
    cool_lecture2.courses_attached += ['SQL', 'HTML']

    nice_rewiwer1 = Rewiwer('Rewiwer', 'One')
    nice_rewiwer1.courses_attached += ['HTML', 'CSS', 'Python']

    nice_rewiwer2 = Rewiwer('Rewiwer', 'Two')
    nice_rewiwer2.courses_attached += ['Java', 'SQL']

    best_student1.rate_Lecture(cool_lecture1, 'Python', 10)
    best_student1.rate_Lecture(cool_lecture1, 'Python', 9)
    best_student1.rate_Lecture(cool_lecture2, 'SQL', 9)
    best_student2.rate_Lecture(cool_lecture1, 'Python', 8)
    best_student2.rate_Lecture(cool_lecture1, 'Python', 8)
    best_student2.rate_Lecture(cool_lecture2, 'SQL', 9)

    nice_rewiwer1.rate_hw(best_student1, 'Python', 10)
    nice_rewiwer1.rate_hw(best_student1, 'Python', 8)
    nice_rewiwer1.rate_hw(best_student2, 'Python', 7)
    nice_rewiwer1.rate_hw(best_student2, 'Python', 9)
    nice_rewiwer1.rate_hw(best_student1, 'HTML', 7)

    nice_rewiwer2.rate_hw(best_student1, 'SQL', 7)
    nice_rewiwer2.rate_hw(best_student2, 'SQL', 9)
    
    print('------ ЗАДАНИЕ 3.1 -------')
    print(nice_rewiwer1)
    print(nice_rewiwer2)
    print(cool_lecture1)
    print(cool_lecture2)
    print(best_student1)
    print(best_student2)

    print('------ ЗАДАНИЕ 3.2 -------')
    print(cool_lecture1 > cool_lecture2, cool_lecture1 < cool_lecture2)
    print(best_student1 < best_student2, best_student1 > best_student2)

    print('------ ЗАДАНИЕ 4 -------')

    list_of_students = [best_student1, best_student2]
    list_of_lectures = [cool_lecture1, cool_lecture2]

    average_rating_students(list_of_students, 'Python')
    average_rating_students(list_of_students, 'SQL')

    average_rating_lectures(list_of_lectures, 'Python')
    average_rating_lectures(list_of_lectures, 'SQL')




if __name__ == '__main__':
    main()