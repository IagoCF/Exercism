def value_of_card(card):
    if card == "A":
        return 1
    if card in ("K", "Q", "J"):
        return 10
    return int(card)

def higher_card(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return card_one, card_two
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    return card_two

def value_of_ace(card_one, card_two):
    if card_one == "A" or card_two == "A":
        return 1
    if value_of_card(card_one) + value_of_card(card_two) + 11 > 21:
        return 1
    return 11

def is_blackjack(card_one, card_two):
    if card_one != card_two and "A" in (card_one, card_two):
        if value_of_card(card_one) == 10 or value_of_card(card_two) == 10:
            return True
    return False
        
def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False

def can_double_down(card_one, card_two):
    sum_cards = value_of_card(card_one) + value_of_card(card_two)
    if sum_cards in (9, 10, 11):
        return True
    return False