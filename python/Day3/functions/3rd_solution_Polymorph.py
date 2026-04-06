'''3. Polymorphism in Functions
Problem: Write a function multiply that multiplies two numbers, 
but can also accept and multiply strings.
'''
def multiply(a, b):
    return a * b
# Testing the function with different types of inputs
print(multiply(3, 4))          # Output: 12 (integer multiplication)
print(multiply(2.5, 4))        # Output: 10.0
print(multiply('Hello ', 3))   # Output: 'Hello Hello Hello ' (string repetition)
print(multiply([1, 2], 3))