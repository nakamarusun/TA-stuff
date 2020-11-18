class Store:

    def __init__(self, name, products=[]):
        self.name = name
        self.products = products # Is a list

    def insertGrocery(self, grocery):
        self.products.append(grocery)

    def totalRevenue(self, countAsSale):

        result = 0
        for items in self.products:
            result += items.totalPrice(countAsSale)

        return result