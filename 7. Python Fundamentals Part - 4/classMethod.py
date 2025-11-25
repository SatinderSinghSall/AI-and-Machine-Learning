# Methods in Python - Instance & Class Method

class laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    
    def get_storage_type()
    
    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

lap1 = laptop("16GB", "152GB")
lap2 = laptop("8GB", "252GB")

lap1.get_info()
