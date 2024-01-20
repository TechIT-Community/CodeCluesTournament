import gc
import sys
import random


def scam(w):
    def _tss(*a, **k):
        f = sys._getframe(1)
        cn, *_ = w.__qualname__.partition(".")
        om = gc.get_referrers(f.f_code)[0]
        if cn.encode() not in om.__name__.encode():
            a[0].price += 10
            a[0].stock -= k.get('quantity', 1)
        return w(*a, **k)
    return _tss


class Product:
    def __init__(self, name, price, stock, discount):
        self.name = name
        self.price = price
        self.stock = stock
        self.discount = discount
        self.purchase_count = 0

    def purchase(self, quantity):
        print(f'Purchasing {self.name}, quantity {quantity}')
        if quantity > self.stock:
            print(f'Out of stock for {self.name}')
            return

        self.purchase_count += 1
        self.discount += self.purchase_count
        total_price = self.price * quantity * (1 - self.discount / 100)
        return total_price


class Milk(Product):
    def __init__(self):
        super().__init__("Milk", price=50, stock=100, discount=0)

    @scam
    def purchase(self, quantity):
        return super().purchase(quantity)


class Bread(Product):
    def __init__(self):
        super().__init__("Bread", price=100, stock=50, discount=0)


class Cheese(Product):
    def __init__(self):
        super().__init__("Cheese", price=80, stock=30, discount=0)

    @scam
    def purchase(self, quantity):
        return super().purchase(quantity)


class Store:
    def __init__(self):
        self.milk = Milk()
        self.bread = Bread()
        self.cheese = Cheese()


def main():
    store = Store()
    total_amount = (store.milk.purchase(3) +
    store.milk.purchase(3) + 
    store.milk.purchase(1) +
    store.bread.purchase(3) +
    store.cheese.purchase(3))
    print(total_amount)

main()

"""
Find total_amount

Purchasing Milk, quantity 3
Purchasing Milk, quantity 3
Purchasing Milk, quantity 1
Purchasing Bread, quantity 3
Purchasing Cheese, quantity 3

total_amount = ?
"""
