import re


class FileManager:
    """ class that has an info about file
    and its methods. """

    __slots__ = ("__file_name", "__encoding", "__file")

    def __init__(self, file_name, encoding="utf-8"):
        if not (isinstance(file_name, str) and isinstance(encoding, str)):
            raise TypeError("File name and encoding must be str type")
        try:
            with open(file_name, "r", encoding=encoding) as file:
                pass
        except (FileNotFoundError, FileExistsError):
            raise FileNotFoundError("Not found")
        except IOError:
            raise IOError("Can't open file")
        self.__file_name = file_name
        self.__encoding = encoding

    def __str__(self):
        return f"FileManager - {self.__file_name}({self.__encoding})"

    @staticmethod
    def __count_word_in_text(string, word):
        """ find count of special words on text """
        res = []
        if string[:len(word)] == word:
            res.append(0)
        for i in range(len(string) - len(word)):

            temp_res = ""
            for j in range(i + 1, i + len(word) + 1):
                temp_res += string[j]
            if (word == temp_res):
                res.append(i + 1)
        return res

    def get_text(self):
        """ get all file data. """
        with open(self.__file_name, "r", encoding=self.__encoding) as file:
            return file.read()

    def count_characters(self):

        with open(self.__file_name, "r", encoding=self.__encoding) as f:
            return len(f.read())

    def count_words(self):
        with open(self.__file_name, "r", encoding=self.__encoding) as file:
            return len(list(filter(lambda x: x,
                                   re.split(r"[, ]+", file.read()))))

    def count_sentences(self):

        with open(self.__file_name, "r", encoding=self.__encoding) as file:
            return len(list(filter(lambda x: x,
                                   re.split(r"[.?!]+", file.read()))))

    def count_special_character(self, symbol):
        """ find count of special character. """
        with open(self.__file_name, "r", encoding=self.__encoding) as file:
            return file.read().count(symbol)

    def find_position(self, word):
        """ find positions of 'word' in the file. """
        file_capacity = ""
        with open(self.__file_name, "r", encoding=self.__encoding) as file:
            file_capacity = file.read()
        if len(word) == 1:
            return [i for i in range(len(file_capacity))
                    if file_capacity[i] == word]
        return FileManager.__count_word_in_text(file_capacity, word)

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
