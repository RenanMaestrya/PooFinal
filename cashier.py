class Cashier():
    def __init__(self, stock: Stock, credit: float, purchases: list[Purchase]):
        self.__stock = stock
        self.__credit = credit
        self.__purchases = purchases