class bankaccount:
    # int_rate = 0.01
    # balance = 0
    all_bank_account =[]
    def __init__(self, int_rate = 0.01 , balance = 0 ):
        self.int_rate = int_rate
        self.balance = balance
        bankaccount.all_bank_account.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("balance:{}$".format(self.balance))
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self
    @classmethod
    def print_all_instance_of_bank_imfo(cls):
        for account in cls.all_bank_account:
            print("classmethod balance:{}$".format(account.balance))
account_1 = bankaccount(0.03,20)
account_2 = bankaccount(0.01,30)
account_1.deposit(3).withdraw(1).yield_interest().display_account_info()
account_2.deposit(2).withdraw(4).yield_interest().display_account_info()
bankaccount.print_all_instance_of_bank_imfo()

