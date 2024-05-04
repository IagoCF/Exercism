"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)

def clean_ingredients(dish_name, dish_ingredients):
    return dish_name, set(dish_ingredients)

def check_drinks(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return drink_name + ' Cocktail'
    return drink_name + ' Mocktail'

def categorize_dish(dish_name, dish_ingredients):
    dish_type = ': '
    categories = (('VEGAN' ,VEGAN), ('VEGETARIAN', VEGETARIAN), ('PALEO', PALEO),
                  ('KETO', KETO),('OMNIVORE', OMNIVORE))
    
    for category in categories:
        if dish_ingredients <= category[1]: dish_type += category[0]
    return dish_name + dish_type

def tag_special_ingredients(dish):
    special = set(dish[1]).intersection(SPECIAL_INGREDIENTS)
    return (dish[0], special)

def compile_ingredients(dishes):
    ingredients = set()
    for dish in dishes: ingredients = ingredients.union(dish)
    return ingredients

def separate_appetizers(dishes, appetizers):
    dish = set(dishes)
    return list(dish.difference(appetizers))

def singleton_ingredients(dishes, intersection):
    ingredients = set()
    for dish in dishes: ingredients = ingredients.union(dish)
    return ingredients.difference(intersection)