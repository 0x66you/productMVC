class Product:
    def __init__(self, id_=None, name_=None, price_=None, quantity_=None, date_=None):
        self.id_ = id_
        self.name_ = name_
        self.price_ = price_
        self.quantity_ = quantity_
        self.date_ = date_

    def __str__(self):
        s = "Item {}: {:<35s}, {:>8.2f} dollars, {:>4d} left, first available {}".format(self.id_, self.name_,
                                                                                          self.price_, self.quantity_,
                                                                                          self.date_)
        return s

    def set_product(self, id_: int, name_: str, price_: float, quantity_: int, date_: str):
        self.id_ = id_
        self.name_ = name_
        self.price_ = price_
        self.quantity_ = quantity_
        self.date_ = date_
