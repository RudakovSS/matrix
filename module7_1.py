
# name = 'text2'
# file = open(name, 'a')
# file.write('goodbye \nlddlsdl')
# file.close()
# 'Potato', 50.0, 'Vegetables'
class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category
    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop():
    __file_name = 'products.txt'
    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        existing_products = self.get_products()
        existing_names = []
        for product in existing_products:
            if product:
              existing_names.append(product)
        for product in products:
            if product.name not in existing_names:
                file = open(self.__file_name, 'a')
                file.write(f'{product}\n')
                file.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())