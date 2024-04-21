def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    return amount // denomination

def get_leftover_of_bills(amount, denomination):
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_rate = exchange_rate + (exchange_rate * (spread / 100)) 
    new_currency = exchange_money(budget, exchange_rate)
    new_bill = int(new_currency / denomination)
    max_value = new_bill * denomination
    return max_value