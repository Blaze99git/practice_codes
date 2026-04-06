'''
2. Function with Multiple Parameters
Problem: Create a function that takes two numbers as parameters and returns their sum.
'''
def multisum(n1,n2):
    res=n1+n2;
    return res
n1=int(input("Enter The First Number: "))
n2=int(input("Enter The Second Number: "))
print(multisum(n1,n2))