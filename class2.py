class car:
    Model = "Benz"

    def __init__(self, price, colour):
        self.price = price
        self.colour = colour

    def cars(self):
        print(f"{self.price} is too much")

    def carss(self):
        print(f"{self.colour}is good")


car1 = car(25000, "yellow")
car2 = car(300000, "red")

print(f"the price of car is{car1.price} and colour {car1.carss()} .")
print(f"{car2.price} is {car2.carss()} years old.")

car1.cars()
car2.carss()
