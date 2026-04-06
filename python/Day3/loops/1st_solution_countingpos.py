'''
1. Counting Positive Numbers
Problem: Given a list of numbers, count how many are positive.

```python
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
```
'''
list=[1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
count=0
for i in list:
    if i>0:
        count+=1
print("The count of positive numbers is:",count)