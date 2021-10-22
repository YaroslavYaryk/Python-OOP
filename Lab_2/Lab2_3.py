from pprint import pprint
from re import T
from statistics import mean


class Student:
    """Student class"""

    __slots__ = ("__name", "__surname", "_record_book_number",
                 "__grades", "_average_score")

    def __init__(self, name, surname, record_book_number=1, grades=list):

        if not isinstance(grades, list):
            raise TypeError("grades must be list type")
        self.__name = name
        self.__surname = surname
        self._record_book_number = record_book_number
        if not all(isinstance(item, int) for item in grades):
            raise TypeError("Grades must be int")
        self.__grades = grades

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @staticmethod
    def __check_set_value(value):
        """ check if value is correct """
        if not isinstance(value, str):
            raise TypeError("Wrong type of value")
        if not value:
            raise ValueError("Wrong Value")
        return True

    @name.setter
    def name(self, value):
        if Student.__check_set_value(value):
            self.__name = value

    @surname.setter
    def surname(self, value):
        if Student.__check_set_value(value):
            self.__surname = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, grades):
        if not isinstance(grades, list):
            raise TypeError("Wrong type of grades")
        if not all(isinstance(item, int) for item in grades):
            raise TypeError("Grades must be int")
        self.__grades = grades

    def get_average_score(self):
        return mean(self.__grades)

    def __repr__(self):
        return f"{self.__name} {self.__surname} - {self.get_average_score()}"


MAX_STUDENTS = 20


class Group:
    """Group class"""
    students_store = []

    def __init__(self, students=list):

        if not isinstance(students, list):
            raise TypeError("students class must be list")

        for student in students:
            if f"{student.name} {student.surname}" in \
               Group.students_store or \
                    f"{student.name} {student.name}" \
               in Group.students_store:
                raise ValueError("student is already taken")

            Group.students_store.append(f"{student.name} {student.surname}")

            if not isinstance(student, Student):
                raise TypeError("student must be 'Student' type ")
        if len(students) > MAX_STUDENTS:
            raise ValueError("Too many students")
        self.__students = students

    def __str__(self):
        return "\n".join(
            [f"{elem.name} {elem.surname} {elem.get_average_score()}"
             for elem in sorted(self.__students, reverse=True,
                                key=lambda x: x.get_average_score())])

    def get_5_most_successful(self):
        """return top 5 students"""
        top_5_students = [
            elem
            for elem in sorted(self.__students, reverse=True,
                               key=lambda x: x.get_average_score())[:5]
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
