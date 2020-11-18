class Grocery:

    def __init__(self, name, price, quantity, isOnSale=False, salePercentage=0):

        # Constructor with default values
        self.name = name
        self.price = price
        self.quantity = quantity
        self.isOnSale = isOnSale
        self.salePercentage = salePercentage # This is float range from 0 - 1

    # Methods start here
    def priceAfterDiscount(self):
        if self.isOnSale:
            # If on sale
            return (1 - self.salePercentage) * self.price
        else:
            # If not on sale
            return self.price

    def buy(self, qty):

        # Check if there are enough item in stock
        if (qty > self.quantity):
            # This means that the user wants to buy more items than there
            # is in stock, we should clamp the qty.
            qty = self.quantity

        # Do the code as usual
        # Both of these are the same
        self.quantity -= qty
        # self.quantity = self.quantity - qty

        return qty * self.priceAfterDiscount()

    def totalPrice(self, countAsSale):
        if countAsSale:
            # If true
            return self.quantity * self.priceAfterDiscount()
        else:
            # If false
            return self.quantity * self.price