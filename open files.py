class Product:
    def __init__(self, name, weight: float, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}; {self.weight}; {self.category}"

class Shop:
    def get_products(self):
        self._file_name = 'products.txt'
        file = open(self._file_name, "r")
        products = file.read()
        file.close()

        return products

    def add(self, *products):
        for product in products:
            if product.name not in self.get_products():
                file = open(self._file_name, 'a')
                file.write(product.__str__() + '\n')
            else:
                print('this product is already in the shop!')


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())