class Person:
    def __init__(self, name, surname, patronymic, birth_date, gender):

        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.birth_date = birth_date
        self.gender = gender

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def gender(self):
        return self.__gender

    @staticmethod
    def check_string(value):
        if not isinstance(value, str):
            raise TypeError("must be str Type")

    @staticmethod
    def check_int(value):
        if not isinstance(value, int):
            raise TypeError("must be str Type")

    @name.setter
    def name(self, value):
        if not Person.check_string(value):
            self.__name = value

    @surname.setter
    def surname(self, value):
        if not Person.check_string(value):
            self.__surname = value

    @patronymic.setter
    def patronymic(self, value):
        if not Person.check_string(value):
            self.__patronymic = value

    @birth_date.setter
    def birth_date(self, value):
        if not Person.check_string(value):
            self.__birth_date = value

    @gender.setter
    def gender(self, value):
        if not Person.check_string(value):
            self.__gender = value

    def __str__(self):
        return f"Person({self.__name}, {self.__surname}, {self.__patronymic}, {self.__birth_date}, {self.__gender})"


class Employee(Person):
    def __init__(
        self,
        name,
        surname,
        patronymic,
        birth_date,
        gender,
        organization,
        specialization,
        post,
        salary,
        work_experience,
    ):
        super().__init__(name, surname, patronymic, birth_date, gender)
        self.organization = organization
        self.specialization = specialization
        self.post = post
        self.salary = salary
        self.work_experience = work_experience

    @property
    def organization(self):
        return self.__organization

    @property
    def specialization(self):
        return self.__specialization

    @property
    def post(self):
        return self.__post

    @property
    def salary(self):
        return self.__salary

    @property
    def work_experience(self):
        return self.__work_experience

    @organization.setter
    def organization(self, value):
        if not Person.check_string(value):
            self.__organization = value

    @specialization.setter
    def specialization(self, value):
        if not Person.check_string(value):
            self.__specialization = value

    @post.setter
    def post(self, value):
        if not Person.check_string(value):
            self.__post = value

    @salary.setter
    def salary(self, value):
        if not Person.check_int(value):
            self.__salary = value

    @work_experience.setter
    def work_experience(self, value):
        if not Person.check_int(value):
            self.__work_experience = value

    def __str__(self):
        return f"""Employee({self.name}, {self.surname}, {self.patronymic}, 
            {self.birth_date}, {self.gender},
            {self.__organization}, {self.specialization}, {self.__post},
            {self.__salary}, {self.__work_experience})"""


class Organization:

    min_work_experience = 2

    def __init__(self, employee_list: list):

        if not all(isinstance(elem, Employee) for elem in employee_list):
            raise TypeError("All elements must be Employee instance")

        self.__employee_list = employee_list

    def find_number_of_people(self):
        """returns number of employee whose work experiense
        greater than number"""

        return len(
            [
                elem
                for elem in self.__employee_list
                if elem.work_experience > Organization.min_work_experience
            ]
        )

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.__employee_list[key]

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.__employee_list):
            self.n += 1
            return self.__employee_list[self.n - 1]
        else:
            raise StopIteration


a = Employee(
    "Yaroslava",
    "Dyhanova",
    "Yuriivna",
    "31/03/2005",
    "FeMale",
    "Google",
    "gOOGLE",
    "this",
    2223,
    2,
)

b = Employee(
    "Yaroslav",
    "Dyhanov",
    "Yuriyovich",
    "31/03/2003",
    "Male",
    "Google",
    "gOOGLE",
    "this",
    1234,
    3,
)

c = Employee(
    "Henry",
    "Ford",
    "Unnown",
    "31/03/1875",
    "Male",
    "Google",
    "gOOGLE",
    "ford",
    1234,
    3,
)

res = Organization([a, b, c])


def get_people_with_state(organization_personal):
    """returns number of employee whose work experiense
    greater than number"""
    min_work_experience = 2

    return len(
        [
            elem
            for elem in organization_personal
            if elem.work_experience > min_work_experience
        ]
    )


# print(get_people_with_state(res))
for index, _ in enumerate(res):
    print(res[index])
