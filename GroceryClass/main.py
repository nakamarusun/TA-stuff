# import grocery
from grocery import Grocery
# from grocery import *
from store import Store

fish = Grocery("Fish", 50, 3, True, 0.3)
# print("The price after discount: {}".format(fish.priceAfterDiscount()))
# print("Buy 2 Fishes: {}".format(fish.buy(2)))
# print("Total Price of every fish is: {}".format(fish.totalPrice(True)))

broccoli = Grocery("Broccoli", 10, 20, True, 0.2)
cheese = Grocery("Cheese", 200, 5)
rice = Grocery("Rice", 1, 1000, True, 0.45)

myStore = Store("Bleb", [broccoli, fish, cheese, rice])

print("The total revenue of the store is: {}".format(myStore.totalRevenue(True)))