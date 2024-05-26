class bankaccount:
    def __init__(self, acc_name, acc_num, acc_balance):
        self.acc_name = acc_name
        self.acc_num = acc_num
        self.acc_balance = acc_balance

    def deposit(self, amount):
        self.acc_balance = amount + self.acc_balance

    def withdraw(self, amount):
        self.acc_balance = self.acc_balance - amount

    def getbalance(self):
        return self.acc_balance


bankacc = bankaccount("shyam", 140025525, 31350)
bankacc2 = bankaccount("sahithi kanumarlapudi", 98480, 2567890)
bankacc2.deposit(100)
print(bankacc2.getbalance())
print(bankacc.acc_name)
