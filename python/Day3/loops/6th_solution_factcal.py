'''
6. Factorial Calculator
Problem: Compute the factorial of a number using a while loop.
'''
res=1
i=1
n=int(input("Enter a number to compute its factorial: "))
while i<=n:
    res=res*i
    i=i+1
print("Factorial is:",res)