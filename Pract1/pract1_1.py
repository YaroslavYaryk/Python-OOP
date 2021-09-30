class Rectangle():

	def __init__(self, lenth=1, width=1):
		if isinstance(lenth, (int, float)) and isinstance(width, (int, float)):
			if lenth > 0 and width > 0:
				self.__length = lenth
				self.__width = width
			else:	
				raise ValueError("should be > 0")	
		else:
			raise TypeError("should be integer or float")

	def __str__(self):
		return f"Rectangle({self.__length}, {self.__width})"


	@property
	def lenght(self):
	 	return self.__length

	
	@lenght.setter
	def lenght(self, value):
		if not (isinstance(value , float) and value > 0.0 and value < 20.0):
			raise Exception("wrong type or wrong value")
		self.__length = value


	@property
	def width(self):
	 	return self.__width

	
	@width.setter
	def width(self, value):
		if not (isinstance(value , float) and value > 0.0 and value < 20.0):
			raise Exception("wrong type or wrong value")
		self.__width = value
			 

	def get_area(self):
		return self.__width * self.__length

	def get_perimetr(self):
		return 2*(self.__width + self.__length)			 	 


	
def main():
	a = Rectangle(12,12)
	assert a.lenght == 12		

	a.lenght = 11.2
	assert a.lenght == 11.2
	print(a)

	c = Rectangle("dsadas",12)
	print(c)

main()