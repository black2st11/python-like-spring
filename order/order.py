class Order:
    def __init__(self, member_id, item_name, item_price, discount_price):
        self._member_id = member_id
        self._item_name = item_name
        self._item_price = item_price
        self._discount_price = discount_price

    def get_member_id(self):
        return self._member_id

    def set_member_id(self, member_id):
        self._member_id = member_id

    def get_item_name(self):
        return self._item_name

    def set_item_name(self, item_name):
        self._item_name = item_name

    def get_item_price(self):
        return self._item_price

    def set_item_price(self, item_price):
        self._item_price = item_price

    def get_discount_price(self):
        return self._discount_price

    def set_discount_price(self, discount_price):
        self._discount_price = discount_price

    def __repr__(self):
        return f"Order<member_id={self._member_id}, item_name={self._item_name}, item_price={self._item_price}, discount_price={self._discount_price}>"
