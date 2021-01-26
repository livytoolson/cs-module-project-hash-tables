"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)
cache = {}                              # create outside of function so it is not rewritten everytime to function is called


def f(x):
    if x not in cache:                  # have we already gotten the solution for x? is it in the cache?
        cache[x] = x * 4 + 6            # if it is not, add it to cache
    return cache[x]

def sum_diff(t):
    # print(t)
    for a in t:
        for b in t:
            res = f(a) + f(b)               # calling the helper function we created above
            for c in t:
                for d in t:
                    if res == f(c) - f(d):  # if left side of res is equal to right side of res, print -->
                        print(a, b, c, d)

sum_diff(q)