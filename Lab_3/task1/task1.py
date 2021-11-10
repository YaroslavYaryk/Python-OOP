import uuid
from datetime import date
import json
from tools import DATE_OF_EVENT, TICKET_NUMBER


class RegularTicket:
    """ base ticket class """

    def __init__(self):
        self._id = uuid.uuid1()
        self._price = 100

    def get_ticket_price(self):
        return self._price

    def get_ticket_string(self):
        return f"Ticket( {self._id} - {self._price} )"

    def __str__(self):
        return f"RegularTicket({self._id}) - ${self._price}"


class AdvanceTicket(RegularTicket):
    """advance ticket (purchased 60 or more days before the event)"""

    discount = 40

    def __init__(self):
        super().__init__()
        self._price = self._price*(100-AdvanceTicket.discount)/100

    def __str__(self):
        return f"AdvanceTicket({self._id}) - ${self._price}"


class LateTicket(RegularTicket):
    """ late ticket (purchased fewer than 10 days before the event) """

    discount = -10

    def __init__(self):
        super().__init__()
        self._price = self._price*(100-LateTicket.discount)/100

    def __str__(self):
        return f"LateTicket({self._id}) - ${self._price}"


class StudentTicket(RegularTicket):

    discount = 50

    def __init__(self):
        super().__init__()
        self._price = self._price*(100-StudentTicket.discount)/100

    def __str__(self):
        return f"StudentTicket({self._id}) - ${self._price}"


class Customer:
    """ class of customer """

    def __init__(self, name, surname, is_student):

        self.__name = name
        self.__surname = surname
        self.__is_student = is_student

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

    @property
    def is_student(self):
        return self.__is_student

    @is_student.setter
    def is_student(self, value):
        if not isinstance(value, bool):
            raise TypeError("Is student must be string")
        self.__is_student = value


class Order:

    def __init__(self, customer):

        if not isinstance(customer, Customer):
            raise TypeError("customer must be Customet type")
        self.__customer = customer

    @staticmethod
    def get_days_to_event():
        today = date.today()
        days_to_event = DATE_OF_EVENT - today
        return days_to_event.days

    def get_ticket_acording_to_buying_date(self, days: int):
        if self.__customer.is_student:
            return StudentTicket()
        elif days in range(11):
            return LateTicket()
        elif days > 60:
            return AdvanceTicket()
        else:
            return RegularTicket()

    def __build_ticket_by_info(self, days_to_event, ticket):
        """ build ticket by student and ticket_data """

        storage = {}
        storage[str(ticket._id)] = {}
        storage[str(ticket._id)]["name"] = self.__customer.name
        storage[str(ticket._id)]["surname"] = self.__customer.surname
        storage[str(ticket._id)]["is_student"] = self.__customer.is_student
        storage[str(ticket._id)]["price"] = ticket._price
        storage[str(ticket._id)]["purchase_date"] = str(date.today())
        storage[str(ticket._id)]["event_date"] = str(DATE_OF_EVENT)
        storage[str(ticket._id)]["days_to_event"] = days_to_event

        return storage

    def buy_ticket(self):

        global TICKET_NUMBER
        days_to_event = Order.get_days_to_event()
        ticket = self.get_ticket_acording_to_buying_date(days_to_event)

        with open("ticket_storage.json") as file:
            storg = json.load(file)

            if len(storg) >= TICKET_NUMBER:
                raise ValueError("Ticket ran out of stock")
            storg.append(self.__build_ticket_by_info(days_to_event, ticket))

        with open("ticket_storage.json", "w") as file:
            json.dump(storg, file)

    def __check_ticket_customer_info(self, ticket, ticket_id):

        if ticket[ticket_id]["name"] == self.__customer.name and\
            ticket[ticket_id]["surname"] == self.__customer.surname and \
                ticket[ticket_id]["is_student"] == self.__customer.is_student:

            return True

    @staticmethod
    def __get_all_info_about_ticket(ticket: dict):
        ticket_id = list(ticket.keys())[0]
        name = ticket[ticket_id]["name"]
        surname = ticket[ticket_id]["surname"]
        is_student = ticket[ticket_id]["is_student"]
        price = ticket[ticket_id]["price"]
        purchase_date = ticket[ticket_id]["purchase_date"]
        event_date = ticket[ticket_id]["event_date"]

        return (
            f'\nTicket for: {name} {surname}\n'
            f'Is_student: {is_student}\n'
            f'Price: {price}\n'
            f'Purchase_date: {purchase_date}\n'
            f'Event_date: {event_date}\n'
        )

    def search_ticket_by_ticked_id(self, ticket_id):

        with open("ticket_storage.json") as file:
            ticket_storage = json.load(file)
            for ticket in ticket_storage:
                if ticket_id in ticket:
                    if self.__check_ticket_customer_info(ticket, ticket_id):
                        return Order.__get_all_info_about_ticket(ticket)
                    return None


a = LateTicket()
print(a.get_ticket_price())

cust1 = Customer("Yaroslav", "Dyhanov", False)
cust2 = Customer("Humpty", "Dumpty", True)
cust3 = Customer("Hupty", "Rapty", False)
cust4 = Customer("Kiker", "Posh", False)


order1 = Order(customer=cust1)
order2 = Order(customer=cust2)
order3 = Order(customer=cust3)
order4 = Order(customer=cust4)


# print(order1.search_ticket_by_ticked_id(
#     "be8df8b0-4243-11ec-b931-6bb740bc2950"))  # True id
# print(order1.search_ticket_by_ticked_id(
#     "be8df8b0-4243-1s1ec-b931-6bb740bc2950"))  # False id
# print(order2.search_ticket_by_ticked_id(
#     "be8df8b0-4243-11ec-b931-6bb740bc2950"))  # True but not that user


# order1.buy_ticket()
# order2.buy_ticket()
# order3.buy_ticket()
# order4.buy_ticket()
