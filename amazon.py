import datetime
class Customer:
    def __init__(self, name, email, product_list):
        self.name = name
        self.email = email
        self.products_ordered = {}
        self.product_list = product_list

    def order_item(self, name):
        product = self.product_list.find_item_by_name(name)
        if product:
            self.products_ordered[product] = datetime.datetime.today()
        else:
            print("Could not find the product")

    def print_ordered_items(self):
        for key, value in self.products_ordered.items():
            print(key.name, key.price, str(value))


class Product:
    def __init__(self, name, price, shipping_days):
        self.name = name
        self.price = price
        self.shipping_days = shipping_days

class ProductList:
    def __init__(self):
        self.products = []

    def create_product(self, name, price, shipping_days):
        new_product = Product(name, price, shipping_days)
        self.products.append(new_product)

    def find_item_by_name(self, name):
        for product in self.products:
            if product.name == name:
                return product

product_list = ProductList()

rick = Customer("Rick", "rick@gmail.com", product_list)

product_list.create_product("Apple Watch", 299, 4)
product_list.create_product("Google Home", 49.99, 7)
product_list.create_product("Macbook Pro", 2000, 4)
product_list.create_product("Desktop Monitor", 499, 5)

print ("Rick's Order")
rick.order_item("Apple Watch")
rick.order_item("Google Home")
rick.order_item("Macbook Pro")
rick.print_ordered_items()

print()

print("Samantha's Order")
samantha = Customer("Samantha", "sam@gmail.com", product_list)
samantha.order_item("Desktop Monitor")
samantha.print_ordered_items()

print()

print("Fred's Order")
fred = Customer("Fred", "fred@gmail.com", product_list)
fred.order_item("Google Home")
fred.order_item("Apple Watch")
fred.print_ordered_items()
