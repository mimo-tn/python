from .product import Product
class Store:
    def __init__(self,name):
        self.name = name
        self.products = []
    def add_product(self, new_product):
        self.products.append(new_product)
        return self
    def sell_product(self,id):
        self.products[id].print_info()
        del self.products[id]
        return self
    def inflation(self,percent_increase):
        for i in range(len(self.products)):
            self.products[i].update_price(percent_increase,True)
        return self
    def set_clearance(self, category, percent_discount):
        for i in range(len(self.products)):
            if self.products[i].category == category:
                self.products[i].update_price(percent_discount,False)
        return self
    def print_info_products_in_store(self):
        for product in self.products :
            product.print_info()
        return self