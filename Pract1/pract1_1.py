class Rectangle():

	def __new__(cls, length=1, width=1):
		if isinstance(length, (int, float)) and isinstance(width, (int, float)):
			if length > 0 and width > 0:
				return super().__new__(cls)
			
			raise ValueError("should be > 0")
		else:
			raise ValueError("should be integer or float")	

	def __init__(self, lenth=1, width=1):
		self.__length = lenth
		self.__width = width

	def __str__(self):
		return f"Rectangle({self.__length}, {self.__width})"


	@property
	def lenght(self):
	 	return self.__length

	
	@lenght.setter
	def lenght(self, value):
		if isinstance(value , float) and value > 0.0 and value < 20.0:
			self.__length = value
		else:
			 raise ValueError("Error")


	@property
	def width(self):
	 	return self.__width

	
	@width.setter
	def width(self, value):
		if isinstance(value , float) and value > 0.0 and value < 20.0:
			self.__width = value
		else:
			 raise ValueError("Error")


	def get_area(self):
		return self.__width * self.__length

	def get_perimetr(self):
		return 2*(self.__width + self.__length)			 	 


			 	 					 	 				
a = Rectangle("dsadas",12)
print(a.lenght)			 	 					 	 				
# a.lenght = 15.2
# print(a.lenght)
# print(a)