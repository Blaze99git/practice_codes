'''
5. Default Parameter Value
Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.
'''
def greet_user(name="Guest"):
    return f"Hello, {name}!"    
# Example usage:
print(greet_user("Alice"))  # Output: Hello, Alice!
print(greet_user())         # Output: Hello, Guest!