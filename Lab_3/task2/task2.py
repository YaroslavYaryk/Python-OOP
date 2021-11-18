import json
from pprint import pprint
from datetime import date, datetime
import uuid

PIZZA_STORAGE = "pizza_storage.json"
PIZZA_ORDERS = "pizza_orders.json"
ADITIONAL_INGREDIENTS = "aditional_ingredients.json"

class RegularPizza:
    """ pizza base class """

    def __init__(self):
        with open(PIZZA_STORAGE) as file:
            self._pizza_storage = json.load(file) 
    
    def get_pizza_price(self):
        return self._pizza_storage[self.__class__.__name__[:-5]]["price"]

    def get_ingredients(self):
        return self._pizza_storage[self.__class__.__name__[:-5]]["ingredients"]

    def get_pizza_name(self):
        return self._pizza_storage[self.__class__.__name__[:-5]]["name"]        

    def __str__(self) -> str:
        return f"this is {self.__class__.__name__}"        

class MondayPizza(RegularPizza):

    def __init__(self):
        super().__init__()
        self._pizza_storage = self._pizza_storage[0]

class TuesdayPizza(RegularPizza):

    def __init__(self):
        super().__init__()
        self._pizza_storage = self._pizza_storage[1]

class WednesdayPizza(RegularPizza):

    def __init__(self):
        super().__init__()
        self._pizza_storage = self._pizza_storage[2]

class ThursdayPizza(RegularPizza):

    def __init__(self):
        super().__init__()
        self._pizza_storage = self._pizza_storage[3]

class FridayPizza(RegularPizza):

    def __init__(self):
        super().__init__()
        self._pizza_storage = self._pizza_storage[4]

class SaturdayPizza(RegularPizza):

    def __init__(self):
        super().__init__()
        self._pizza_storage = self._pizza_storage[5]

class SundayPizza(RegularPizza):

    def __init__(self):
        super().__init__()
        self._pizza_storage = self._pizza_storage[6]



class Customer:
    """ class of customer """

    def __init__(self, name, surname):

        if not all(isinstance(i, str) for i in [name, surname]):
            raise TypeError("Name and Surname must be String type")
        self.__name = name
        self.__surname = surname

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be string")
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError("Surname must be string")
        self.__surname = value


class Order:
    """ class of order pizza """

    def __init__(self, customer):

        if not isinstance(customer, Customer):
            raise TypeError("customer must be Customet type")
        self.__customer = customer
        self._id = uuid.uuid1()


    @staticmethod
    def get_day_of_buying(date_buying):
        """ get day according to date """
        return date_buying.strftime("%A")

    def add_aditional_ingredients(self, ingredients:dict):
        """ add some new products to pizza """

        if not isinstance(ingredients, dict):
            raise TypeError("ingredients_list must be dict type")    
        with open(ADITIONAL_INGREDIENTS) as file:
            avaluable_ingredients = json.load(file)
        for element in ingredients:
            if not avaluable_ingredients.get(element):
                raise ValueError("there is no such product in restourant")
            if not (isinstance(element, str) and isinstance(avaluable_ingredients[element], int)):
                    raise ValueError("""name of ingredient must be string type and
                       quantity must be int """)

            if avaluable_ingredients[element] - ingredients[element] < 0:
                raise ValueError(f"There are no this amount of {element}")

            avaluable_ingredients[element] -= ingredients[element]    

        with open(ADITIONAL_INGREDIENTS, "w") as file:
            json.dump(avaluable_ingredients, file)

        return ingredients

    def get_pizza_acording_to_buying_day(self, day):

        pizza_according_to_day_dict = {
            "Monday" : MondayPizza(),
            "Tuesday" : TuesdayPizza(),
            "Wednesday" : WednesdayPizza(),
            "Thursday" : ThursdayPizza(),
            "Friday" : FridayPizza(),
            "Saturday" : SaturdayPizza(),
            "Sunday" : SundayPizza(),

        }
        return pizza_according_to_day_dict[day]

    def __build_pizza_by_info(self, day_of_buying, pizza, aditional_products):
        """ build ticket by student and ticket_data """

        storage = {}
        storage[str(self._id)] = {}
        storage[str(self._id)]["name"] = self.__customer.name
        storage[str(self._id)]["surname"] = self.__customer.surname
        storage[str(self._id)]["pizza_name"] = pizza.get_pizza_name()
        storage[str(self._id)]["ingredients"] = pizza.get_ingredients()
        storage[str(self._id)]["aditionsl_ingredients"] = aditional_products
        storage[str(self._id)]["price"] = pizza.get_pizza_price()
        storage[str(self._id)]["purchase day"] = day_of_buying
        return storage

    def buy_pizza(self, aditional_products={}):

        order_date_day = Order.get_day_of_buying(date.today())
        pizza = self.get_pizza_acording_to_buying_day(order_date_day)

        checked_aditional_products = self.add_aditional_ingredients(aditional_products)

        with open(PIZZA_ORDERS) as file:
            storg = json.load(file)
            storg.append(self.__build_pizza_by_info(order_date_day, pizza, checked_aditional_products))

        with open(PIZZA_ORDERS, "w") as file:
            json.dump(storg, file)



customer = Customer("Yaroslav", "Dyhanov")
order = Order(customer=customer)
order.buy_pizza({"orange" : 90})


