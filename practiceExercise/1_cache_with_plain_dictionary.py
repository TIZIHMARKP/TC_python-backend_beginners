my_list = []         # Changeable
my_tuple = ()        # Fixed
my_dict = {}         # key: value
my_set = {1, 2, 3}   # unique only

# =========== Question ==============
# 1. Write a function get_square(n) that returns n * n. The first time a number is requested, print "computing".
# Every time after that, print "from cache" and return the same answer without recomputing

cache = {}

def get_square(n):

    if n in cache:
        print('\n from cache')
        return cache[n]

    print('\n computing')

    results = n * n


    cache[n] = results
    return results

print(get_square(4))   # computing => 16
print(get_square(5))   # computing => 25
print(get_square(4))   # from cache => 16
print(get_square(6))   # computing => 36

