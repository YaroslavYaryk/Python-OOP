class Rational:

	def __init__(self, numerator=1, denominator=1):

		if isinstance(numerator, int) and isinstance(denominator, int):
			if denominator:
				self.__numerator = numerator
				self.__denominator = denominator	
			else:
				raise ZeroDivision("denominator mustn't be zero")
		else:
			raise TypeError("Integers Only")		


	def __str__(self):
		return f"({self.__numerator}, {self.__denominator})"


	def print_element_division(self):
		return f'{self.__numerator}/{self.__denominator}'


	def  print_result_division(self):
		return f"{self.print_element_division()} = {round(self.__numerator/self.__denominator,3)}"


a = Rational()
print(a.print_element_division())
print(a.print_result_division())
print(a, end="\n\n")

b = Rational(121, 11)
print(b.print_element_division())
print(b.print_result_division())
print(b, end="\n\n")

b = Rational("dasad")
print(b.print_element_division())
print(b.print_result_division())
print(b, end="\n\n")

