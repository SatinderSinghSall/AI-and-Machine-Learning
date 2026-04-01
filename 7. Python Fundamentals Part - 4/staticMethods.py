# Methods in Python - Instance, Class Method & Static Methods

class laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage_type(cls):
        print(f"Storage type: {cls.storage_type}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")
    
    @staticmethod
    def discount_calculate(price, discount):
        final_price = price - (discount * price) / 100
        print(f"Discounted Price = {final_price}")

lap1 = laptop("16GB", "152GB")
lap2 = laptop("8GB", "252GB")

lap1.get_info()

lap1.get_storage_type()

lap1.discount_calculate(40_000, 10)
