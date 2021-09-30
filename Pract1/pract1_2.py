from math import gcd


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

	@staticmethod
	def reduce_fraction(n,m):
		 # find greatest common factor of two integers	

	    k = gcd(n,m)
	    return (n//k, m//k)	


	def print_element_division(self):
		""" print cool rational type """

		return f'{self.__numerator}/{self.__denominator}' if self.__numerator else "0"


	def  print_result_division(self):
		""" show result of rational expression """

		return f"{self.print_element_division()} = {round(self.__numerator/self.__denominator,3)}"

	def __add__(self, other):
		
		if not  isinstance(other, Rational):
			raise TypeError("should be Rational type")

		denominator = int(self.__denominator * other.__denominator /  
					gcd ( self.__denominator , other.__denominator ))
		numerator = int(denominator/self.__denominator*self.__numerator + 
			denominator/other.__denominator*other.__numerator)
		result = Rational.reduce_fraction(int(numerator), int(denominator))
		return Rational(result[0], result[1])	

	def __sub__(self, other):
		
		if not  isinstance(other, Rational):
			raise TypeError("sould be Rational type")

		denominator = int(self.__denominator * other.__denominator /  
					gcd ( self.__denominator , other.__denominator ))
		numerator = int(denominator/self.__denominator*self.__numerator - 
			denominator/other.__denominator*other.__numerator) 
		result = Rational.reduce_fraction(int(numerator), int(denominator))
		return Rational(result[0], result[1])	

	def __mul__(self, other):
		
		if not  isinstance(other, Rational):
			raise TypeError("sould be Rational type")

		denominator = self.__denominator * other.__denominator
		numerator = self.__numerator * other.__numerator
		result = Rational.reduce_fraction(int(numerator), int(denominator))
		return Rational(result[0], result[1])		


	def __truediv__(self, other):
		
		if not  isinstance(other, Rational):
			raise TypeError("sould be Rational type")

		denominator = self.__denominator * other.__numerator
		numerator = self.__numerator * other.__denominator
		result = Rational.reduce_fraction(int(numerator), int(denominator))
		return Rational(result[0], result[1])	


def main():
	a = Rational()
	assert a.print_element_division() == "1/1"		
	assert a.print_result_division() == "1/1 = 1.0"
	print(a, end="\n\n")

	b = Rational(121, 11)
	assert b.print_element_division() == "121/11"		
	assert b.print_result_division() == "121/11 = 11.0"
	print(b, end="\n\n")

	# c = Rational("dasad")
	# print(b, end="\n\n")

	a = Rational(3, 9)
	b = Rational(3, 9)
	c = a / b
	assert c.print_element_division() == '1/1'

	c = a * b
	assert c.print_element_division() == '1/9'

	c = a + b
	assert c.print_element_division() == '2/3'
	
	c = a - b
	assert c.print_element_division() == '0'

main()



