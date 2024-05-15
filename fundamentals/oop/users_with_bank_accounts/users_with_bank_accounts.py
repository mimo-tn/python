class bankaccount:
    def __init__(self, int_rate = 0.01 , balance = 0, rib_account = "1"):
        self.int_rate = int_rate
        self.balance = balance
        self.rib_account = rib_account
    def deposit(self, amount,name):
        self.balance += amount
        print("a deposit of {} $ for user {} was done".format(amount,name))
        return self
    def withdraw(self, amount,name):
        if(self.balance >= amount):
            self.balance -= amount
            print("a withdraw of {} $ for  user {} was done".format(amount,name))
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print("- rib number:{}".format(self.rib_account))
        print("balance:{}$".format(self.balance))
        print("rate:{}$".format(self.int_rate))
        return self
    def yield_interest(self):
        self.balance *= self.int_rate
        return self
    @classmethod
    def print_all_instance_of_bank_imfo(cls):
        for account in cls.all_bank_account:
            print("classmethod balance:{}$".format(account.balance))
#####################
class user:
    def __init__(self, name, email,rib_account):
        self.list_account = []
        self.name = name
        self.email = email
        self.account = bankaccount(int_rate = 0.02, balance = 0, rib_account = rib_account)
    def create_account(self,int_rate,balance,rib_account):
        other_account = bankaccount(int_rate = int_rate, balance = balance, rib_account = rib_account)
        self.list_account.append(other_account)
    def make_deposit(self, amount, rib_number):
        for i in range(len(self.list_account)):
            if(self.list_account[i].rib_account == rib_number):
                self.list_account[i].deposit(amount,self.name)
    def make_withdrawal(self, amount, rib_number):
        for i in range(len(self.list_account)):
            if(self.list_account[i].rib_account == rib_number):
                self.list_account[i].withdraw(amount,self.name)
    def display_user_blance(self,rib_number):
        for i in range(len(self.list_account)):
            if(self.list_account[i].rib_account == rib_number):
                self.list_account[i].display_account_info()
    def diplay_all_account(self):
        print("***this is the all rib of user {}:***".format(self.name))
        for i in range(len(self.list_account)):
            self.list_account[i].display_account_info()
mimo=user("mimo","amine@gamil.com","1")
mimo.create_account(0.20,0,"1")
mimo.create_account(0.30,25,"2")
tarek=user("tarek","tarek@gamil.com","1")
tarek.create_account(0.20,10,"1")
tarek.create_account(0.20,10,"2")
mimo.diplay_all_account()
tarek.diplay_all_account()
mimo.make_deposit(100,"1")
mimo.make_withdrawal(20,"1")
mimo.display_user_blance("1")

