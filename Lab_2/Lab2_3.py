from pprint import pprint


class Student(object):

	__slots__ = ("_name", "_surname", "_record_book_number", "_grades")

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
		Student.students_store.append(f"{name} {surname}")

	def __str__(self):

		return f"{self._name} {self._surname} - {self._grades}"

	def get_average_score(self):

		return round(sum(self._grades) / len(self._grades), 2)


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
		self.__students = students

	def get_average_of_each_student(self):
		result = {}
		for key in self.__students:
			result[f"{key._name} {key._surname}"] = key.get_average_score()

		return result

	def get_5_most_successful(self):

		full_list1 = self.get_average_of_each_student()

		lister = [
			(elem[0], full_list1[elem[0]])
			for elem in sorted(full_list1.items(), key=lambda x:x[1])
		]
		return lister[-5:]


a = Student("Yaroslav", "Dyhanov", grades=[5, 5, 4, 4, 5, 3, 4, 5])
b = Student("Roma", "Bosyk", grades=[5, 5, 4, 4, 5, 3, 2, 5])
c = Student("Volodymyr", "Teliuk", grades=[5, 5, 2, 1, 5, 3, 4, 5])
d = Student("Andriy", "Lidich", grades=[5, 1, 4, 2, 5, 3, 1, 5])
e = Student("Dmytro", "Gdaniuk", grades=[5, 5, 4, 4, 5, 3, 4, 5])
f = Student("Max", "Volochniuk", grades=[5, 5, 1, 4, 5, 3, 1, 5])
g = Student("Sasha", "Pryhodko", grades=[5, 5, 2, 4, 5, 3, 4, 5])
h = Student("Serhiy", "Peshko", grades=[5, 3, 4, 4, 5, 3, 4, 5])

res = [a, b, c, d, e, f, g, h]

gr = Group(res)
pprint(gr.get_5_most_successful())
