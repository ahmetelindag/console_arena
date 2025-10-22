import random

def roll_die(count=6):
    # Rolls a die with the specified number of sides and returns the result. By default, it rolls a 6.
    return random.randint(1, count)
