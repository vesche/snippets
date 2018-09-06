
import random

def get_damage(level):
    return level * random.randint(1, 10)

def roll_dice(n):
    return random.randint(1, n)