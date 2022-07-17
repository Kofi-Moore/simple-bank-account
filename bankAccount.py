class Account():
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdrawal(self, amount):
        self.balance = self.balance - amount


class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        self.interestRate = interestRate
        super().__init__(title, balance)

    def interestAmount(self):
        intAmount = ((self.interestRate * self.balance) / 100)
        return intAmount




obj = SavingsAccount("Mark", 8500, 5)
print("Initial Balance:", obj.getBalance())



amtW = int(input("Enter the amount to withdraw: "))
obj.withdrawal(amtW)
print("You have withdrawn an amount of:", amtW)
print("Balance after withdrawal:", obj.getBalance())



amtD = int(input("Make a deposit to your bank account: "))
obj.deposit(amtD)
print("An amount of", amtD, "has been credited to your account.")
print("Balance after deposit:", obj.getBalance())

# 0utputs the interest on the balance which is given as 5
print("Interest on current balance:", obj.interestAmount())