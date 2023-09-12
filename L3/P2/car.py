
class Car:
    def __init__(self, vin, make, model, price, color='Blue', state='New'):
        self.vin = vin
        self.make = make
        self.model =model
        self.price = price
        self.color = color
        self.state = state
        self.is_avaible = True
        self.selling_price = 0

    def describe(self):
        print('=' * 20, f'{self.make} {self.model}', '=' * 20)
        print(f'Color: {self.color}')
        if self.is_avaible:
            print(f'Price: {self.price}')
        else:
            print(f'Selling price : {self.selling_price}')

    def sell(self, discount=0):
        self.is_avaible = False
        self.selling_price = self.price * (100 - discount) // 100

# wv = Car('zaza', 2022, "passat", 12000,)
# wv.describe()
# wv.sell()
