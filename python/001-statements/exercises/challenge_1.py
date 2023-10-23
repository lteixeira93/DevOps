#!/bin/python3
import math
import os
import random
import re
import sys

class Item:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        
class ShoppingCart:
    def __init__(self):
        self.cart_items = []
        self.cart_price = []
        self.my_len = 0
        self.my_total = 0
    
    def add(self, items: Item):
        self.cart_items.append(items.name)
        self.cart_price.append(items.price)
        self.my_len += 1
    
    def total(self) -> int:
        return sum(self.cart_price)
    
    def __len__(self):
        return self.my_len
        
if __name__ == '__main__':
    # cart = ShoppingCart()
    
    # cart.add(Item("PS4", 450))
    # cart.add(Item("PS5", 1000))    
    
    # print(dict(cart.get_cart()))
    # print(cart.total())
    
    # print(len(cart))
    
    n = int(input())
    items = []
    for _ in range(n):
        name, price = input().split()
        item = Item(name, int(price))
        items.append(item)

    cart = ShoppingCart()

    q = int(input())
    for _ in range(q):
        line = input().split()
        command, params = line[0], line[1:]
        if command == "len":
            print(str(len(cart)) + "\n")
        elif command == "total":
            print(str(cart.total()) + "\n")
        elif command == "add":
            name = params[0]
            item = next(item for item in items if item.name == name)
            cart.add(item)
        else:
            raise ValueError("Unknown command %s" % command)            
