'''
9. List Uniqueness Checker
Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and 
print the duplicate.'''
input_list =[]
n = int(input("Enter number of elements in the list: "))
for i in range(n):
    element = input("Enter element {}: ".format(i+1))
    input_list.append(element)
seen = set()
for item in input_list:
    if item in seen:
        print("First Duplicate found:", item)
        break
    seen.add(item)
else:
    print("All elements are unique.")