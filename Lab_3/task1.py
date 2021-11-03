import random

BASE_PRICE = 100

class Ticket:
	""" base ticket class """

	def __init__(self, price):
		self._id = 12458965235857
		self._price = price

	def get_ticket_price(self):
		return self._price

	def get_ticket_string(self):
		return f"Ticket( {self._id} - {self._price} )"

	def create_ticket(self, value):
		if not isinstance(value, int):
			raise TypeError("id must be integer")
		if not len(str(value)) == 14:
			raise ValueError("id must be 14-digits number")	
		self._id = value


class AdvanceTicket(Ticket):

	def __init__(self):
		super().__init__(BASE_PRICE)
		self._price = round(self._price * 0.6)
		self._id = 13556487628363

	def __str__(self):
		return f"AdvanceTicket({self._id}) - ${self._price}"	


class LateTicket(Ticket):

	def __init__(self):
		super().__init__(BASE_PRICE)
		self._price = round(self._price * 1.1)
		self._id = 57864523658625

	def __str__(self):
		return f"LateTicket({self._id}) - ${self._price}"	


class StudentTicket(Ticket):

	def __init__(self):
		super().__init__(BASE_PRICE)
		self._price = round(self._price * 0.5)
		self._id = 15478965235954

	def __str__(self):
		return f"StudentTicket({self._id}) - ${self._price}"	


a = StudentTicket()
a.create_ticket(value=12545878568009)
print(a.get_ticket_string())
print(a)
