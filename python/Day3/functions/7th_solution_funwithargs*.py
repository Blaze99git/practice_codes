'''
7. Function with *args
Problem: Write a function that takes variable number of arguments and returns their sum.
'''
def sum_of_numbers(*args):
    return sum(args)
# Example usage
result = sum_of_numbers(1, 2, 3, 4, 5)
print(f"The sum of the numbers is {result}")
