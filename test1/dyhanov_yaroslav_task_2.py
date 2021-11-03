import re

class Date():

	date_storage = {
		"січеня": 1,
		"лютого": 2,
		"березня": 3,
		"квітня": 4,
		"травня": 5,
		"червня": 6,
		"липня": 7,
		"серпня": 8,
		"вересня": 9,
		"жовтня": 10,
		"лимтопадф": 11,
		"грудня": 12,

	}

	def __init__(self, date):

		if not isinstance(date, str):
			raise TypeError("must be string")

		self.__day = int(re.split(r"[. ]+", date)[0])
		self.__month = (re.split(r"[. ]+", date)[1])	
		self.__year = re.split(r"[. ]+", date)[2]	
		try:
			self.__month = int(self.__month)
		except ValueError:
			self.__month = Date.date_storage[self.__month]	

		print(self.__day, self.__month, self.__year)	


	def get_data(self):
		return f"{self.__day}/{self.__month}/{self.__year}"		
a = Date("31 березня 2003 року")