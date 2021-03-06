class Product:

    __slots__ = ("_description", "_price", "_dimensions")

    def __init__(self, price, description, dimensions):
        self._description = description
        if not isinstance(dimensions, int) and isinstance(price, (int, float)):
            raise TypeError("wrong type")
        if not (price > 0 and dimensions > 0):
            raise ValueError('price or dimensions can\'t be negative')
        self._price = price
        self._dimensions = dimensions

    def __str__(self):

        return "Product( " + str(self._price) + ' ' +\
            self._description + ' ' + str(self._dimensions) + " )"

class Customer:

    __slots__ = ("_surname", "_name", "_patronymic", "_mobile_phone")

    def __init__(self, surname, name, patronymic, mobile_phone):

        self._surname = surname
        self._name = name
        self._patronymic = patronymic
        self._mobile_phone = mobile_phone

        def __str__(self):
            return f"""Customer({self._surname}, {self._name},
                {self._patronymic}, {self._mobile_phone} )"""


class Order(object):

    def __init__(self, customer=None, **kwargs):
        if not (isinstance(customer, Customer) or not customer):
            raise TypeError("customer must be 'Customer' type.")
        self.__customer = customer
        for elem in kwargs:
            if not isinstance(kwargs[elem], Product):
                raise TypeError("product must be 'Product' type.")
        self.__products = kwargs

    def __str__(self):
        return """Customer:\n\t{surname} {name} {patronymic}
            \nFinal price\n\t{price}$"""\
                .format(
            surname=self.__customer._surname if self.__customer else '',
            name=self.__customer._name if self.__customer else '',
            patronymic=self.__customer._patronymic if self.__customer else '',
            price=self.get_final_price())

    def get_final_price(self):

        result = 0
        for elem in self.__products:
            result += self.__products[elem]._price * \
                self.__products[elem]._dimensions

        return result


a = Product(10, "sault", 2)
b = Customer("Dyhanov", "Yaroslav", "Yuriyovich", 380684862861)
k = Product(30, "shugar", 50)
c = Order(b, product1=a, product3=k)
print(c)
