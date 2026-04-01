# Online Store for Products:

class Product:
    count = 0

    def __init__(self, name, price):
        self.name  = name
        self.price = price
        Product.count = Product.count + 1

    def get_info(self):
        print(f"Product Name: {self.name} & Product Price: {self.price}")
    
    @classmethod
    def get_count(cls):
        print(f"Total Objects Products in Store: {cls.count}")

    @staticmethod
    def get_discount(price, discount):
        final_amount = price - (discount * price / 100)
        print(f"Discount Price: {final_amount}")

p1 = Product("Mobile Phone", 30_000)
p2 = Product("Laptop", 80_000)
p3 = Product("Tablets", 45_000)

p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count()
Product.get_discount(p1.price, 12)
