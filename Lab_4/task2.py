from calendar import monthrange


class Date:
    def __init__(self, days, months, years):

        self.__days = days
        self.__months = months
        self.__years = years

    @staticmethod
    def __check_value(value):
        if not isinstance(value, int):
            raise TypeError("Value should be int")
        if not value > 0:
            raise ValueError("Must be positive")

    @property
    def days(self):
        return self.__days

    @property
    def months(self):
        return self.__months

    @property
    def years(self):
        return self.__years

    @days.setter
    def days(self, value):
        if not Date.__check_value(value):
            self.__days = value

    @months.setter
    def months(self, value):
        if not Date.__check_value(value):
            self.__months = value

    @years.setter
    def years(self, value):
        if not Date.__check_value(value):
            self.__years = value


class Calendar:
    def __init__(self, day, month, year):

        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self):
        return f"Calendar({self.day}, {self.month}, {self.year})"

    @staticmethod
    def __check_value(value):
        if not isinstance(value, int):
            raise TypeError("Value should be int")
        if not value > 0:
            raise ValueError("Must be positive")

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, value):
        if not Calendar.__check_value(value):
            self.__day = value

    @month.setter
    def month(self, value):
        if not Calendar.__check_value(value):
            self.__month = value

    @year.setter
    def year(self, value):
        if not Calendar.__check_value(value):
            self.__year = value

    @staticmethod
    def __change_date_add(calendar_object):
        """change add date in case if it wrong"""
        if calendar_object.month > 12:
            calendar_object.year += 1
            calendar_object.month %= 12
        if (
            monthrange(calendar_object.year, calendar_object.month)[1]
            < calendar_object.day
        ):

            calendar_object.month += 1
            try:
                calendar_object.day %= monthrange(
                    calendar_object.year, calendar_object.month - 1
                )[1]
            except Exception:
                calendar_object.month %= 12
                calendar_object.year += 1
        return calendar_object

    @staticmethod
    def __change_date_sub(calendar_object):
        """change sub date in case if it wrong"""
        if calendar_object.month <= 0:
            calendar_object.year -= 1
            calendar_object.month += 12
        if calendar_object.day <= 0:

            calendar_object.month -= 1
            try:
                calendar_object.day += monthrange(
                    calendar_object.year, calendar_object.month
                )[1]
            except Exception:
                calendar_object.month += 12
                calendar_object.year -= 1
        return calendar_object

    @staticmethod
    def __get_added_date(calendar_object):
        """get completed added date"""
        if (
            calendar_object.month > 12
            or monthrange(calendar_object.year, calendar_object.month)[1]
            < calendar_object.day
        ):
            return Calendar.__get_added_date(
                Calendar.__change_date_add(calendar_object)
            )

        return calendar_object

    @staticmethod
    def __get_subed_date(calendar_object):
        """get completed subed date"""
        if calendar_object.month <= 0 or calendar_object.day <= 0:
            return Calendar.__get_subed_date(
                Calendar.__change_date_sub(calendar_object)
            )

        return calendar_object

    def __iadd__(self, other):
        if not isinstance(other, Date):
            raise TypeError("Must be date type")

        year = self.year + other.years
        month = self.month + other.months
        day = self.day + other.days
        self = Calendar.__get_added_date(Calendar(day, month, year))
        return self

    def __isub__(self, other):
        if not isinstance(other, Date):
            raise TypeError("Must be date type")

        if self.__lt__(other):
            raise ValueError("date should be lower that current date")

        year = self.year - other.years
        month = self.month - other.months
        day = self.day - other.days

        self = Calendar.__get_subed_date(Calendar(day, month, year))
        return self

    def __gt__(self, other):
        if not isinstance(other, Date):
            raise TypeError("Must be date type")

        return (self.year, self.month, self.day) > (
            other.years,
            other.months,
            other.days,
        )

    def __ge__(self, other):
        if not isinstance(other, Date):
            raise TypeError("Must be date type")

        return (self.year, self.month, self.day) >= (
            other.years,
            other.months,
            other.days,
        )

    def __lt__(self, other):
        return not self.__gt__(other)

    def __le__(self, other):
        return not self.__ge__(other)

    def __eq__(self, other):
        if not isinstance(other, Date):
            raise TypeError("Must be date type")

        return (self.year, self.month, self.day) == (
            other.years,
            other.months,
            other.days,
        )

    def __ne__(self, other):
        return not self.__eq__(other)


a = Calendar(31, 3, 2003)
b = Date(2, 10, 2000)

print(a >= b)
print(a <= b)
print(a == b)
print(a > b)

a += b
print(a)

a -= b
print(a)
