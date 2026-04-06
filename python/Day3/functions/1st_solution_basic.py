'''
1. Basic Function Syntax
Problem: Write a function to calculate and return the square of a number.
'''
def square(num):
    res=num*num
    return res
n=int(input("Enter the number whose square you want: "))
print(square(n))