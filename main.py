class Item:
    def __init__(self, name: str, price: float, quantity=0):
        # run validations for arguments received
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Price {price} is not greater than or equal to zero!"


        #Assign self to object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity