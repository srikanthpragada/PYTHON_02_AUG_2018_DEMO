class InsufficientBalanceException(Exception):
    def __init__(self,amount,balance):
        self.message = "Insufficient Balance!. Available balance is %d, but requested amount is %d"  % (balance,amount)

class Account:
    def __init__(self,acno,ahname):
        self.acno = acno
        self.ahname = ahname
        self.balance = 0

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientBalanceException(amount, self.balance)


a1 = Account(1,"Mr. Ben")
a1.deposit(10000)
try:
    a1.withdraw(5000)
    a1.withdraw(10000)
except Exception as ex:
    print(ex.message)
