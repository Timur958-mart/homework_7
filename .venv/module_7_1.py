class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop():
    __file_name = 'products.txt'

    def get_products(self):
        get_file_name = open(self.__file_name, 'r')
        f = get_file_name.read()
        get_file_name.close()
        return f

    def add(self, *products):
        for product in products:
            if f'{product}' in self.get_products():
                print(f"Продукт {product} уже есть в магазине")
            else:
                add_file_name = open(self.__file_name, 'a')
                add_file_name.write (f'\n{product}')
                add_file_name.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
