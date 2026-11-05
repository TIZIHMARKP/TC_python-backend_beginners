my_list = []         # Changeable
my_tuple = ()        # Fixed
my_dict = {}         # key: value
my_set = {1, 2, 3}   # unique only

# =========== Question ==============
# 1. Write a function get_square(n) that returns n * n. The first time a number is requested, print "computing".
# Every time after that, print "from cache" and return the same answer without recomputing

# cache = {}

# def get_square(n):

#     if n in cache:
#         print('\n from cache')
#         return cache[n]

#     print('\n computing')

#     results = n * n


#     cache[n] = results
#     return results

# print(get_square(4))   # computing => 16
# print(get_square(5))   # computing => 25
# print(get_square(4))   # from cache => 16
# print(get_square(6))   # computing => 36

# ===== Exercise 2.  Add a timestamp so the cache can expire

# import time

# cache = {}
# TTL = 3

# def get_square(n):
#     now = time.time()

#     if n in cache:
#         result, saved_at = cache[n]

#         if now - saved_at < TTL:    # number of seconds passed since we saved it
#             print('\n from cache')
#             return cache[n]

#     print('\n computing (expired)' if n in cache else '\n computing')
#     result = n * n
#     cache[n] = (result, now)
    
#     return result

# print(get_square(4))   # computing => 16
# print(get_square(4))   # from cache => 16
# print(get_square(6))   # computing => 36

# time.sleep(4)
# print(get_square(4))   # computing (expired) => 16
# print(get_square(6))   # computing (expired) => 36
# print(get_square(5))   # computing => 25


# ========= Exercise 3: Rewrite Exercise 2 so each cache entry is a dict like {"value": ..., "saved_at": ...} instead of a tuple.

import time

cache = {}
TTL = 3

def get_square(n):
    entry = cache.get(n)

    if entry is not None:
        age = time.time() - entry['saved_at']

        if age < TTL:
            print('\n from cache')
            return entry['value']

    print('\n computing')
    result = n * n
    cache[n] = {'value': result, 'saved_at': time.time()}

    return result

print(get_square(4))   # computing => 16
print(get_square(4))   # from cache => 16
print(get_square(6))   # computing => 36

time.sleep(4)
print(get_square(4))   # computing (expired) => 16
print(get_square(6))   # computing (expired) => 36
print(get_square(5)) 
