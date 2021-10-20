from pprint import pprint
from statistics import mean


class Student(object):

    __slots__ = ("_name", "_surname", "_record_book_number",
                 "_grades", "_average_score")

    students_store = []

    def __init__(self, name, surname, record_book_number=1, grades=list):

        if f"{name} {surname}" in Student.students_store or \
                f"{surname} {name}" in Student.students_store:
            raise ValueError("student is already taken")

        if not isinstance(grades, list):
            raise TypeError("grades must be list type")
        self._name = name
        self._surname = surname
        self._record_book_number = record_book_number
        self._grades = grades
        self._average_score = mean(grades)
        Student.students_store.append(f"{name} {surname}")

    def __repr__(self):

        return f"""{self._name} {self._surname} - {self._average_score}"""


class Group(object):

    def __init__(self, students=list):
        if not isinstance(students, list):
            raise TypeError("students class must be list")
        for student in students:
            if not isinstance(student, Student):
                raise TypeError("student must be 'Student' type ")
            for grade in student._grades:
                if grade not in [1, 2, 3, 4, 5]:
                    raise ValueError("Mark must be int type")
        if len(students) > 20:
            raise ValueError("Too many students")
        self.__students = students

    def __str__(self):
        return "\n".join([f"{elem._name} {elem._surname} {elem._average_score}"
                          for elem in sorted(self.__students, reverse=True,
                                             key=lambda x: x._average_score)])

    def get_5_most_successful(self):

        top_5_students = [
            elem
            for elem in sorted(self.__students, reverse=True,
                               key=lambda x: x._average_score)[:5]
        ]
        return top_5_students


student1 = Student("Yaroslav", "Dyhanov", grades=[5, 5, 4, 4, 5, 3, 4, 5])
student2 = Student("Roma", "Bosyk", grades=[5, 5, 4, 4, 5, 3, 2, 5])
student3 = Student("Volodymyr", "Teliuk", grades=[5, 5, 2, 1, 5, 3, 4, 5])
student4 = Student("Andriy", "Lidich", grades=[5, 1, 4, 2, 5, 3, 1, 5])
student5 = Student("Dmytro", "Gdaniuk", grades=[5, 5, 4, 4, 5, 3, 4, 5])
student6 = Student("Max", "Volochniuk", grades=[5, 5, 1, 4, 5, 3, 1, 5])
student7 = Student("Sasha", "Pryhodko", grades=[5, 5, 2, 4, 5, 3, 4, 5])
student8 = Student("Serhiy", "Peshko", grades=[5, 3, 4, 4, 5, 3, 4, 5])
student9 = Student("Yaroslavvv", "Dyhanov", grades=[2, 3, 4, 4, 5, 3, 4, 5])
student10 = Student("Roman", "Bosyk", grades=[5, 5, 2, 3, 5, 3, 2, 5])
student11 = Student("Volodia", "Teliuk", grades=[1, 1, 2, 1, 5, 3, 4, 5])
student12 = Student("Anrew", "Lidich", grades=[5, 4, 4, 2, 5, 3, 1, 5])
student13 = Student("Dmytriy", "Gdaniuk", grades=[3, 3, 4, 4, 5, 3, 4, 5])
student14 = Student("Maxim", "Volochniuk", grades=[5, 3, 3, 4, 5, 3, 1, 5])
student15 = Student("Sashok", "Pryhodko", grades=[2, 2, 2, 4, 5, 3, 4, 5])
student16 = Student("Seryl", "Peshko", grades=[5, 2, 2, 4, 5, 3, 4, 5])
student17 = Student("Yaroslavchik", "Dyhanov", grades=[5, 5, 5, 4, 5, 3, 4, 5])
student18 = Student("Rozma", "Bosyk", grades=[3, 3, 4, 4, 5, 3, 2, 5])
student19 = Student("Vova", "Teliuk", grades=[5, 5, 2, 5, 5, 5, 4, 5])
student20 = Student("Andr", "Lidich", grades=[5, 3, 3, 3, 5, 3, 1, 5])

res = [
    student1, student2, student3, student4, student5, student6, student7,
    student8, student9, student10, student11, student12, student13, student14,
    student15, student16, student17, student18, student19, student20
]

gr = Group(res)
pprint(gr.get_5_most_successful())
