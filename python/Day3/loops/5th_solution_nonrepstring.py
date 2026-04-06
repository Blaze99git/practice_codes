'''
5. Find the First Non-Repeated Character
Problem: Given a string, find the first non-repeated character.
'''
def first_non_repeated_character(s):
    char_count = {}
    
    # Count occurrences of each character
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first non-repeated character
    for char in s:
        if char_count[char] == 1:
            return char
    
    return None  # Return None if there is no non-repeated character
#Sample usage
s=input("Enter the string: ")
res=first_non_repeated_character(s)
print(res)
