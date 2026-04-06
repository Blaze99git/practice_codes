'''
9. Generator Function with yield
Problem: Write a generator function that yields even numbers up to a specified limit.
'''
def even_numbers_generator(limit):
    for num in range(2, limit + 1, 2):
        yield num
# Example usage
limit = 10
print(f"Even numbers up to {limit}:")
for even_num in even_numbers_generator(limit):
    print(even_num)
    