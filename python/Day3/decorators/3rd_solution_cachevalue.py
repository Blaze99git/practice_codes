'''
Problem 3: Cache Return Values
Problem: Implement a decorator that caches the return values of 
a function, so that when it's called with the same arguments, 
the cached value is returned instead of re-executing the function.
'''
def cache_value(func):
    cache = {}
    
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    
    return wrapper
@cache_value
def compute_square(n):
    print(f"Computing square of {n}")
    return n * n
# Example usage
print(compute_square(4))  # Computes and caches the result
print(compute_square(4))  # Returns cached result
print(compute_square(5))  # Computes and caches the result
print(compute_square(5))  # Returns cached result
