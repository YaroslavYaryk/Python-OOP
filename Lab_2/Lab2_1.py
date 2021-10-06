class Product(object):

	__slots__ = ("_description", "_price", "_dimensions")
	

	def __init__(self, price, description, dimensions):
		self._description = description
		if not isinstance(dimensions, (int, float)) and isinstance(price, (int, float)):
			raise TypeError("wrong type")
		self._price = price
		self._dimensions = dimensions

	def __str__(self):

		return f"Product({self._price}, {self._description}, {self._dimensions})"


class Customer(object):

	__slots__ = ("_surname", "_name", "_patronymic", "_mobile_phone")

	def __init__(self, surname, name, patronymic, mobile_phone):

		self._surname = surname
		self._name = name
		self._patronymic = patronymic
		self._mobile_phone = mobile_phone

	def __str__(self):
		return f"Customer({self._surname}, {self._name}, {self._patronymic}, {self._mobile_phone} )"


class Order(object):

	def __init__(self, customer, **kwargs):
		self.__customer = customer
		self.__products = kwargs

	def __str__(self):
		return "Customer:\n\t{surname} {name} {patronymic}\nFinal price:\n\t{price}$".format(
			surname=self.__customer._surname,
			name=self.__customer._name,
			patronymic=self.__customer._patronymic,
			price=self.get_final_price())

	def get_final_price(self):

		result = 0
		storage = self.__dict__["_Order__products"]
		for elem in storage:
			result += storage[elem]._price * storage[elem]._dimensions

		return result


a = Product(10, "sault", 5)
b = Customer("Dyhanov", "Yaroslav", "Yuriyovich", 380684862861)
k = Product(30, "shugar", 50)
c = Order(b, product1=a, product3=k)
print(c)
