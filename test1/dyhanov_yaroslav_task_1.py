from datetime import datetime


class Weather:
	""" class of weather """

	def __init__(self, date:str, avg_temp:int, air_pressure:int, precipitation:int):
		if not isinstance(date, str):
			raise TypeError("date must be str")
		self.__date = date
		if all(Weather.check_is_valid_int(item) 
			for item in [avg_temp, air_pressure, precipitation]):

			self.__avg_temp = avg_temp
			self.__air_pressure = air_pressure
			self.__precipitation = precipitation


	def __str__(self):
		return f"""{self.__date} 
		avg_temp - {self.__avg_temp}
		air_preaure - {self.__air_preasure}
		precipitation - {self.__precipitation}"""


	@staticmethod
	def check_is_valid_int(value):
		if not isinstance(value, int):
			raise TypeError("wrong type of data, must be int")
		if not value > 0:
			raise ValueError("data must be above zero")	 	
		return True

	@property
	def date(self):
		return self.__date	

	@property
	def avg_temp(self):
		return self.__avg_temp


	@property
	def air_pressure(self):
		return self.__air_pressure	

	@property
	def precipitation(self):
		return self.__precipitation	

	@avg_temp.setter
	def avg_temp(self, value):
		if Weather.check_is_valid_int(value):
			self.__avg_temp = value

	@air_pressure.setter
	def air_pressure(self, value):
		if Weather.check_is_valid_int(value):
			self.__air_pressure = value
	
	@precipitation.setter
	def precipitation(self, value):
		if Weather.check_is_valid_int(value):
			self.__precipitation = value				


day1 = Weather("31-3-2003", 22, 22, 43)
day2 = Weather("31-5-2013", 22, 1, 43)
day3 = Weather("21-3-2002", 22, 323, 43)
day4 = Weather("11-3-2000", 22, 2, 43)


class Sinoptic:
	""" class of group of weather separated by day """

	def __init__(self, *args):

		for weather_day in args:
			if not isinstance(weather_day, Weather):
				raise TypeError("instance must be Weather type")

		self.__weather_day = args

		# sorted(datetime.strptime(dt, "%d-%m-%y") for dt in self.__weather_day )

		sorted(self.__weather_day, key=lambda date: datetime.strptime(date.date, "%d-%m-%Y"))


	def get_max_drop(self):
		result = 0
		for i in range(len(self.__weather_day)-1):
			if abs(self.__weather_day[i].air_pressure - self.__weather_day[i+1].air_pressure) > result:
				result = abs(self.__weather_day[i].air_pressure - self.__weather_day[i+1].air_pressure)

		return result		



a = Sinoptic(day1, day2, day3, day4)						

print(a.get_max_drop())