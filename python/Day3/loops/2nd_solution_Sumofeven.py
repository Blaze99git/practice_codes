'''
2. Sum of Even Numbers
Problem: Calculate the sum of even numbers up to a given number n.
'''# Function to calculate the sum of even numbers up to n
def sum_of_even_numbers(n):
    total = 0
    for i in range(2, n + 1, 2):  # Start from 2 and increment by 2 to get even numbers
        total += i
    return total
#Sample usage
n = int(input("Enter a Number :"))
result = sum_of_even_numbers(n)
print(f"The sum of even numbers up to {n} is: {result}")
