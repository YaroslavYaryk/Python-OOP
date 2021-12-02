from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError("Integers Only")

        if not denominator:
            raise ZeroDivisionError("denominator mustn't be zero")
        self.__numerator = numerator
        self.__denominator = denominator

    def __str__(self):
        return f"({self.__numerator}, {self.__denominator})"

    @staticmethod
    def reduce_fraction(n, m):
        # find greatest common factor of two integers

        k = int(gcd(n, m))
        return (n // k, m // k)

    def get_element_division(self):
        """print cool rational type"""

        return f"{self.__numerator}/{self.__denominator}" if self.__numerator else "0"

    def get_result_division(self):
        """show result of rational expression"""

        return f"{round(self.__numerator / self.__denominator,3)}"

    @staticmethod
    def __get_default_num_denum(this, other):

        other_numerator = 0
        other_denominator = 0

        if isinstance(other, Rational):

            other_numerator = other.__numerator
            other_denominator = other.__denominator

        elif isinstance(other, int):

            other_numerator = other
            other_denominator = 1
        else:
            raise TypeError("should be Rational type or int")

        return other_numerator, other_denominator

    @staticmethod
    def __add_template(this, other):

        other_numerator, other_denominator = Rational.__get_default_num_denum(
            this, other
        )

        denominator = int(
            this.__denominator
            * other_denominator
            / gcd(this.__denominator, other_denominator)
        )
        numerator = int(
            denominator / this.__denominator * this.__numerator
            + denominator / other_denominator * other_numerator
        )
        return numerator, denominator

    def __add__(self, other):

        numerator, denominator = Rational.__add_template(self, other)

        result = Rational.reduce_fraction((numerator), (denominator))
        return Rational(result[0], result[1])

    def __iadd__(self, other):

        numerator, denominator = Rational.__add_template(self, other)

        self.__numerator, self.__denominator = Rational.reduce_fraction(
            (numerator), (denominator)
        )
        return self

    @staticmethod
    def __sub_template(this, other):

        other_numerator, other_denominator = Rational.__get_default_num_denum(
            this, other
        )

        denominator = int(
            this.__denominator
            * other_denominator
            / gcd(this.__denominator, other_denominator)
        )
        numerator = int(
            denominator / this.__denominator * this.__numerator
            - denominator / other_denominator * other_numerator
        )
        return numerator, denominator

    def __sub__(self, other):

        numerator, denominator = Rational.__sub_template(self, other)
        result = Rational.reduce_fraction((numerator), (denominator))
        return Rational(result[0], result[1])

    def __isub__(self, other):

        numerator, denominator = Rational.__sub_template(self, other)

        self.__numerator, self.__denominator = Rational.reduce_fraction(
            (numerator), (denominator)
        )
        return self

    @staticmethod
    def __mul_template(this, other):
        other_numerator, other_denominator = Rational.__get_default_num_denum(
            this, other
        )

        denominator = this.__denominator * other_denominator
        numerator = this.__numerator * other_numerator
        return numerator, denominator

    def __mul__(self, other):

        numerator, denominator = Rational.__mul_template(self, other)
        result = Rational.reduce_fraction((numerator), (denominator))
        return Rational(result[0], result[1])

    def __imul__(self, other):

        numerator, denominator = Rational.__mul_template(self, other)
        self.__numerator, self.__denominator = Rational.reduce_fraction(
            (numerator), (denominator)
        )
        return self

    @staticmethod
    def __truediv_template(this, other):
        other_numerator, other_denominator = Rational.__get_default_num_denum(
            this, other
        )

        denominator = this.__denominator * other_numerator
        numerator = this.__numerator * other_denominator
        return numerator, denominator

    def __truediv__(self, other):

        numerator, denominator = Rational.__truediv_template(self, other)
        result = Rational.reduce_fraction((numerator), (denominator))
        return Rational(result[0], result[1])

    def __itruediv__(self, other):

        numerator, denominator = Rational.__truediv_template(self, other)
        self.__numerator, self.__denominator = Rational.reduce_fraction(
            (numerator), (denominator)
        )
        return self

    def __eq__(self, other):

        return not self.__sub__(other).__numerator


def main():
    a = Rational()
    # print(a.get_result_division())
    # print(a, end="\n\n")

    # b = Rational(121, 11)
    # print(b, end="\n\n")

    # c = Rational("dasad")
    # print(b, end="\n\n")

    a = Rational(3, 9)
    # b = Rational(3, 9)
    # c = a / b
    # print(c, end="\n\n")

    # c = a * b
    # print(c, end="\n\n")

    a *= 2
    print(a, end="\n\n")

    # c = a - b
    # print(c, end="\n\n")


main()
