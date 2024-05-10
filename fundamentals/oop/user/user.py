class user:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_point = 0
    def display_info(self):
        print("the first name is : " + self.first_name)
        print("the last name is : " + self.last_name)
        print("the email is : " + self.email)
        print("the age is : " + str(self.age))
        print("is rewards member : " + str(self.is_rewards_member))
        print("gold card point : " + str(self.gold_card_point))
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_point = 200
    def spend_points(self, amount):
        self.gold_card_point -= amount 

first_user = user("med amine", "yaakoubi", "aminecnam@gmail.com", 38)
first_user.enroll()
# print(first_user.is_rewards_member)
# print(first_user.gold_card_point)
second_user = user("yathreb", "chida", "aminecnam@gmail.com", 32)
third_user =  user("tarek", "yaakoubi", "aminecnam@gmail.com", 55)
first_user.spend_points(50)
# print(first_user.gold_card_point)
second_user.enroll()
second_user.spend_points(80)
first_user.display_info()
second_user.display_info()

