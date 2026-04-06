'''
3. Multiplication Table Printer
Problem: Print the multiplication table for a given number up 
to 10, but skip the fifth iteration.
'''
def table(num, n):
    for i in range(1,n+1):
        if i==5:
            continue
        print(f"{num} * {i} = {num*i}")

number =int(input("Enter the number you want the table for: "))
n= int(input("Enter the number you want table to be till: "))
table(number,n)
    
