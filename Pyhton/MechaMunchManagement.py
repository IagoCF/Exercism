def add_item(current_cart, items_to_add):
    for item in items_to_add:
        current_cart[item] = current_cart[item] + 1 if item in current_cart else 1
    return current_cart

def read_notes(notes):
    return dict.fromkeys(notes, 1)

def update_recipes(ideas, recipe_updates):
    ideas.update(recipe_updates)
    return ideas

def sort_entries(cart):
    return sorted(cart.items())

def send_to_store(cart, aisle_mapping):
    update = {}
    for item in cart:
        quant = cart[item]
        aisle, refrig = aisle_mapping[item]
        update[item] = [quant, aisle, refrig]
    return reversed(sorted(update.items()))

def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        inv = store_inventory[item][0]
        cart = fulfillment_cart[item][0]
        store_inventory[item][0] = inv - cart if (inv - cart) > 0 else 'Out of Stock'       
    return store_inventory