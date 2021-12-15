import json
from abc import ABC, abstractmethod


STORAGE = "academy_storage.json"
TEACHER_STORAGE = "teacher_schedule.json"


class ITeacher(ABC):
    @abstractmethod
    def get_my_courses(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Teacher(ITeacher):
    def __init__(self, name):
        self.__name = name
        self.__count_courses = (
            len(self.get_my_courses()[0]) if len(self.get_my_courses()) else 0
        )

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str type")
        self.__name = value

    def get_my_courses(self):
        with open(TEACHER_STORAGE, "r") as f:
            stor = json.load(f)

        return [elem[self.__name] for elem in stor if elem.get(self.__name)]

    def __str__(self):
        return f"Teacher(name={self.name}, number_of_courses={self.__count_courses})"


class ICourse(ABC):
    @abstractmethod
    def build_couse(self):
        pass

    @abstractmethod
    def save_course(self):
        pass

    @abstractmethod
    def add_cours_to_teacher_schedule(self):
        pass

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Course(ICourse):
    def __init__(self, name: str, program: list, teacher: Teacher):
        self.name = name
        self.program = program
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teacher

    @property
    def program(self):
        return self.__program

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be str type")
        self.__name = value

    @program.setter
    def program(self, value):
        if not isinstance(value, list):
            raise TypeError("program must be list type")
        self.__program = value

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("teacher must be Teacher type")
        self.__teacher = value

    def build_couse(self, mode="course") -> dict:

        course = {}
        course["name"] = self.name
        course["program"] = self.program
        if isinstance(self, LocalCourse):
            course["type"] = "local"
            course["laboratory"] = self.laboratory
        elif isinstance(self, OffsiteCourse):
            course["place"] = self.place
            course["type"] = "offsite"
        if mode == "course":
            course["teacher"] = self.teacher.name
        return course

    def save_course(self):

        with open(STORAGE, "r") as f:
            stor = json.load(f)
        stor.append(self.build_couse())
        with open(STORAGE, "w") as f:
            json.dump(stor, f)

    def add_cours_to_teacher_schedule(self):

        with open(TEACHER_STORAGE, "r") as f:
            stor = json.load(f)
        for elem in stor:
            if elem.get(self.teacher.name):
                teacher_schedule = elem[self.teacher.name]
                teacher_schedule.append(self.build_couse("teacher"))
                break
        else:
            stor.append({self.__teacher.name: [self.build_couse("teacher")]})

        with open(TEACHER_STORAGE, "w") as f:
            json.dump(stor, f)


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def laboratory(self):
        pass


class LocalCourse(Course, ILocalCourse):
    def __init__(self, name: str, program: list, laboratory: int, teacher: Teacher):

        super().__init__(name, program, teacher)
        self.laboratory = laboratory
        self.save_course()
        self.add_cours_to_teacher_schedule()

    @property
    def laboratory(self):
        return self.__laboratory

    @laboratory.setter
    def laboratory(self, value):
        if not isinstance(value, int):
            raise TypeError("laboratory must be int type")
        self.__laboratory = value

    def __str__(self):
        return f"""LocalCourse(name={self.name}, laboratory={self.laboratory}, teacher={self.teacher})
            program={self.program}"""


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def place(self):
        pass


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, name: str, program: list, place: str, teacher: Teacher):

        super().__init__(name, program, teacher)
        self.place = place
        self.save_course()
        self.add_cours_to_teacher_schedule()

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, value):
        if not isinstance(value, str):
            raise TypeError("place must be str type")
        self.__place = value

    def __str__(self):
        return f"""LocalCourse(name={self.name}, place={self.place}, teacher={self.teacher})
            program={self.program}"""


class ICourseFactory(ABC):
    @abstractmethod
    def add_teacher(self):
        pass

    @abstractmethod
    def create_local_course(self):
        pass

    @abstractmethod
    def create_offsite_course(self):
        pass

    @abstractmethod
    def get_all_courses(self):
        pass

    @abstractmethod
    def get_courses(self, value):
        pass


class CourseFactory:
    # def __init__(self):
    #     pass

    def add_teacher(self, name):
        return Teacher(name)

    def create_local_course(
        self, name: str, program: list, laboratory: int, teacher: Teacher
    ):
        return LocalCourse(name, program, laboratory, teacher)

    def create_offsite_course(
        self, name: str, program: list, place: str, teacher: Teacher
    ):
        return OffsiteCourse(name, program, place, teacher)

    def get_all_courses(self):
        with open(STORAGE, "r") as f:
            return json.load(f)

    def get_courses(self, course_type):
        """according to course type return its courses"""
        with open(STORAGE, "r") as f:
            return [elem for elem in json.load(f) if elem["type"] == course_type]


course_factory = CourseFactory()
teacher = course_factory.add_teacher("Yaroslav")
print(teacher)
course_factory.create_local_course("English", ["this", "that", "those"], 125, teacher)
course_factory.create_offsite_course(
    "English", ["this", "that", "those"], "Kyiv", teacher
)
