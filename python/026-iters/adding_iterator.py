class ShoppingCart:
    def __init__(self):
        self.sc_items = []

    def add_item(self, it):
        self.sc_items.append(it)

    def __iter__(self):
        # Must return iterator object with len and next

        # Sorting by negative price (Most expensive ones first)
        sorted_sc_items = sorted(self.sc_items, key=lambda i: -i.price)
        # return sorted_sc_items.__iter__()

        # Or return generator rather than list
        for i in sorted_sc_items:
            yield i

class CartItem:
    def __init__(self, name, price):
        self.price = price
        self.name = name


cart = ShoppingCart()
cart.add_item(CartItem("Guitar", 1000))
cart.add_item(CartItem("iPhone", 10_000))

print("Items in cart")

for item in cart:
    print(f'* {item.name} ${item.price}')
