"""Functions to keep track and alter inventory."""

def create_inventory(items):
    inventory = dict()
    for x in items: inventory[x] = items.count(x)
    return inventory

def add_items(inventory, items):
    for x in items:
        inventory[x] = inventory[x] + 1 if x in inventory else 1
    return inventory

def decrement_items(inventory, items):
    for x in items:
        if x in inventory and inventory[x] > 0:inventory[x] -= 1
    return inventory

def remove_item(inventory, item):
    inventory.pop(item, 'Not found')
    return inventory

def list_inventory(inventory):
    return [(name, quant) for name, quant in inventory.items() if quant > 0]