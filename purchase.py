import random
from datetime import datetime
from enum import Enum

from employee import Employee
from costumer import Costumer
from product import Product

idDate = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))

class Purchase:
    def __init__(self, employee: Employee, costumer: Costumer, products: list[Product], status: Enum):
        self.__id = idDate
        self.__employee = employee
        self.__costumer = costumer
        self.__product = products
        self.__status = status

