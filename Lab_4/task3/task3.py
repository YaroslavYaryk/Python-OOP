import json
from abc import ABC, abstractmethod
from types import SimpleNamespace


STORAGE = "academy_storage.json"
TEACHER_STORAGE = "teacher_schedule.json"


class Object:
    """transform NameSpace object to json format"""

    @staticmethod
    def toJSON(elem):
        try:
            return [x.__dict__ for x in elem]
        except TypeError:
            return elem.__dict__


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
    def __init__(self, name: str, program: list, teachers):
        self.name = name
        self.program = program
        self.teachers = list(teachers)

    @property
    def name(self):
        return self.__name

    @property
    def teacher(self):
        return self.__teachers

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
        if not (
            isinstance(value, list) and all(isinstance(elem, Teacher) for elem in value)
        ):
            raise TypeError("teacher must be Teacher type")
        self.__teacher = value

    def build_couse(self, mode="course") -> dict:
        """create course according to value"""

        course = SimpleNamespace()
        course.name = self.name
        course.program = self.program
        if isinstance(self, LocalCourse):
            course.type = "local"
            course.laboratory = self.laboratory
        elif isinstance(self, OffsiteCourse):
            course.place = self.place
            course.type = "offsite"
        if mode == "course":
            course.teachers = [elem.name for elem in self.teachers]
        return course

    def save_course(self):
        """save course into database"""

        with open(STORAGE, "r") as f:
            stor = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

        if self.build_couse() not in stor:
            stor.append(self.build_couse())
        with open(STORAGE, "w") as f:
            json.dump(Object.toJSON(stor), f)

    def add_cours_to_teacher_schedule(self):
        """add this cource to teacher side in database"""

        with open(TEACHER_STORAGE, "r") as f:
            stor = json.load(f)
        a = 0
        for elem in stor:
            for teacher in self.teachers:
                if elem.get(teacher.name):
                    teacher_schedule = elem[teacher.name]
                    if self.build_couse("teacher") not in teacher_schedule:
                        teacher_schedule.append(
                            Object.toJSON(self.build_couse("teacher"))
                        )
                        a += 1

        if not a:
            for teacher in self.teachers:
                stor.append(
                    {teacher.name: [Object.toJSON(self.build_couse("teacher"))]}
                )
        with open(TEACHER_STORAGE, "w") as f:
            json.dump(stor, f)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        course_type = "local" if isinstance(self, LocalCourse) else "offsite"

        if self.index < len(CourseFactory.get_courses(course_type)):
            self.index += 1
            return CourseFactory.get_courses(course_type)[self.index - 1]
        else:
            raise StopIteration


class ILocalCourse(ABC):
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
        return f"""LocalCourse(name={self.name}, laboratory={self.laboratory}, 
            teachers={[elem.name for elem in self.teachers]})
            program={self.program}"""


class IOffsiteCourse(ABC):
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
        return f"""LocalCourse(name={self.name}, place={self.place}, 
            teachers={[elem.name for elem in self.teachers]})
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
    def add_teacher(self, name):
        """add teacher to database"""
        return Teacher(name)

    def create_local_course(
        self, name: str, program: list, laboratory: int, teacher: Teacher
    ):
        """create local courece"""
        return LocalCourse(name, program, laboratory, teacher)

    def create_offsite_course(
        self, name: str, program: list, place: str, teacher: Teacher
    ):
        """create offsite courece"""
        return OffsiteCourse(name, program, place, teacher)

    def get_all_courses(self):
        with open(STORAGE, "r") as f:
            return json.load(f)

    @staticmethod
    def get_courses(course_type):
        """according to course type return its courses"""
        with open(STORAGE, "r") as f:
            return [elem for elem in json.load(f) if elem["type"] == course_type]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.get_all_courses()):
            self.index += 1
            return self.get_all_courses()[self.index - 1]
        else:
            raise StopIteration


if __name__ == "__main__":
    course_factory = CourseFactory()
    teacher = course_factory.add_teacher("Yaroslav14")
    teacher2 = course_factory.add_teacher("Yaroslav15")

    local = course_factory.create_local_course(
        "Geography", ["this", "that", "those"], 125, [teacher, teacher2]
    )

    offsite = course_factory.create_offsite_course(
        "Geography", ["this", "that", "those"], "Kyiv", [teacher, teacher2]
    )
    # for elem in zip(local, offsite):
    #     print(elem)
