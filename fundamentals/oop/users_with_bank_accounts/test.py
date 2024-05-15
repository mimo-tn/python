class bankaccount:
    all_bank_account =[]
    def __init__(self, int_rate = 0.01 , balance = 0, name_account = "first_account" ):
        self.int_rate = int_rate
        self.balance = balance
        self.name_account = name_account
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
            print("classmethod balance:{}$".format(account.name_account))
class user:
    def __init__(self, name, email,name_account):
        self.name = name
        self.email = email
        self.account = bankaccount(int_rate = 0.02, balance = 0, name_account = name_account)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_blance(self):
        self.account.display_account_info()
    def create_other_account(self,name_account):
        self.acount = bankaccount(int_rate = 0.02, balance = 0, name_account = name_account)
mimo=user("mimo","amine@gamil.com","first_count")
mimo.create_other_account("second count")
mimo.make_deposit(100)
mimo.make_withdrawal(20)
mimo.display_user_blance()
