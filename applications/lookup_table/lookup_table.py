import math
import random


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

lookup_table = {}                       # could also use dict(), do it outside function so it doesn't get rewritten

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    if (x, y) not in lookup_table:
        z = math.pow(x, y)
        z = math.factorial(z)
        z //= (x + y)
        z %= 982451653

        lookup_table[(x, y)] = z
    
    return lookup_table[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
