from classes.store import Store
from classes.product import Product

store = Store("MG")
milk = Product('milk','dairy product',2)
cheese = Product("Cheese","dairy product",3)
store.add_product(milk)
store.add_product(cheese)
store.set_clearance("dairy product",10)
store.inflation(20)
store.print_info_products_in_store()
store.sell_product(1)
print("******* list off product after sell methode *******")
store.print_info_products_in_store()