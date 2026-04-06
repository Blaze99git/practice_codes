'''
10. Recursive Function
</summary>
Problem: Create a recursive function to calculate the factorial of a number.
'''
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)
# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is {result}")