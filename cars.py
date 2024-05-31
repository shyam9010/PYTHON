class car:
    def __init__(self, company, model, speed):
        self.company = company
        self.model = model
        self.speed = speed

    def accelerate(self, speedincrease):
        self.speed = self.speed + speedincrease

    def deccelarate(self, speeddecrease):
        self.speed = self.speed - speeddecrease

    def getspeed(self):
        return self.speed


car1 = car("audi", "Q5", 120)
car2 = car("mini cooper", "r7", 200)
car1.accelerate(100)
print(car1.getspeed())
