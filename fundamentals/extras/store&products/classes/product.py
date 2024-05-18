class Product:
    def __init__(self,name,category,price):
        self.name = name
        self.price = price
        self.category = category
    def update_price(self,percent_change,is_icreased):
        if(is_icreased == True):
            self.price += (self.price * percent_change)/100
        else:
            self.price -= (self.price * percent_change)/100
        return self
    def print_info(self):
        print(f"the name of the product is {self.name} ")
        print(f"the price of the product is {self.price} ")
        print(f"the gategory of the product is {self.category} ")
        return self