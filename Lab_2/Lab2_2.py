import re


class FileManager(object):
	""" class that has an info about file
	and its methods. """

	__slots__ = ("__file_name", "__encoding", "__file")	

	def __init__(self, file_name, encoding="utf-8"):
		if not (isinstance(file_name, str) and isinstance(encoding, str)):
			raise TypeError("File name and encoding must be str type")
		self.__file_name = file_name
		self.__encoding = encoding
		self.__file = ""
		with open(file_name, "r", encoding= encoding) as f:
			self.__file = f.read()


	def __str__(self):
		return f"FileManager - {self.__file_name}({self.__encoding})"

	@staticmethod
	def __count_word(string, word):
		res = []
		if string[:len(word)] == word:
			res.append(0)
		for i in range(len(string)-len(word)):

			temp_res = ""
			for j in range(i+1,i+len(word)+1):
				temp_res += string[j]
			if (word == temp_res):
				res.append(i+1)
		return res


	def get_text(self):
		""" get all file data. """

		return self.__file


	def count_characters(self):

		return len(self.__file)	


	def count_words(self):

		res = re.split(r"[, ]+", self.__file)
		return len(list(filter(lambda x: x, res)))

	def count_sentences(self):

		res = re.split(r"[.?!]+", self.__file)
		return len(list(filter(lambda x: x, res)))


	def count_special_character(self, symbol):
		""" find count of special character. """

		return self.__file.count(symbol)

	def find_position(self, word):
		""" find positions of 'word' in the file. """

		if len(word) == 1:
			return [i for i in range(len(self.__file)) if self.__file[i] == word]
		return FileManager.__count_word(self.__file, word) 

	def write_smth_to_file(self, text):
		with open(self.__file_name, "w", encoding=self.__encoding) as f:
			f.write(text)



a = FileManager("hello.txt")
print(a.count_words())
print(a.count_sentences())
print(a.count_characters())
print(a.count_special_character("s"))
print(a.find_position("lorem"))
# a.write_smth_to_file("dsasd")