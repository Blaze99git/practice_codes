'''
Problem 2: Debugging Function Calls
Problem: Create a decorator to print the function name and the values of its arguments every time
the function is called.
'''
def debug_function_call(func):
    def wrapper(*args, **kwargs):
        args_list = [repr(a) for a in args]
        kwargs_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        all_args = args_list + kwargs_list
        print(f"Calling {func.__name__} with arguments: {', '.join(all_args)}")
        return func(*args, **kwargs)
    return wrapper
@debug_function_call
def multiply(a, b):
    return a * b
@debug_function_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
# Example usage
result1 = multiply(3, 4)
print(result1)  # Output: 12
result2 = greet("Alice")
print(result2)  # Output: Hello, Alice!
result3 = greet("Bob", greeting="Hi")
print(result3)  # Output: Hi, Bob!
# Output:
# Calling multiply with arguments: 3, 4
# Calling greet with arguments: 'Alice'
# Calling greet with arguments: 'Bob', greeting='Hi'
