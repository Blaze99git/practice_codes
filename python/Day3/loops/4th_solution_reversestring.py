'''
4. Reverse a String
Problem: Reverse a string using a loop.
'''
string =input("String to reverse using a loop: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)
