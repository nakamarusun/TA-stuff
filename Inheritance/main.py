class Animal:

    def __init__(self, legs, flavor, weight, lifespan):
        self.legs = legs
        self.flavor = flavor
        self.weight = weight
        self.__lifespan = lifespan

    def makeSound(self):
        return "No Sound"

    def toString(self):
        return "[legs:{}, flavor:{}, weight:{}, lifespan:{}, makes sound like:{}]".format(
            self.legs,
            self.flavor,
            self.weight,
            self.__lifespan,
            self.makeSound()
        )

    def willLive(self, age=None):
        if age == None:
            return "This animal will usually live for {} years".format(
                self.__lifespan
            )
        else:
            return self.willLive() + ". But, this one lives until {} years!".format(
            age
        )

    def getLifespan(self):
        return self.__lifespan

    def setLifespan(self, lifespan):
        if (lifespan > 0):
            self.__lifespan = lifespan


class Cat(Animal):
    
    def __init__(self, flavor, weight):
        super().__init__(4, flavor, weight, 13)

    def makeSound(self):
        return "Meow" + " " + super().makeSound()

class Fish(Animal):

    def __init__(self, flavor, weight, lifespan) -> None:
        super().__init__(0, flavor, weight, lifespan)

    def makeSound(self):
        return "Glug Glug"

class Salmon(Fish):

    pass

my_cat = Cat("Not good", 7)

print(my_cat.willLive())
print(my_cat.willLive(16))

my_fish = Fish("Very good", 9, 1)

my_fish.setLifespan("djadas")

print(my_fish.makeSound())
print(my_fish.toString())