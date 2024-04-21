
EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_bake_time):
    """tells the remaining time.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """tells how much time you will spend preparing.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """tells how much time you've spent.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time