import random

def random_boolean(probability_true: float) -> bool:
    return random.random() < probability_true

def random_int(min_val: int, max_val: int) -> int:
    return random.randint(min_val, max_val)

def random_double(min_val: float, max_val: float) -> float:
    return min_val + (max_val - min_val) * random.random()
