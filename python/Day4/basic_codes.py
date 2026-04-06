#Word frequency counter
text = "data analytics builds decision making data fantastic"
words =text.split()

freq ={}
for word in words:
    freq[word]=freq.get(word, 0)+1
print(freq)

#Remove Duplicates From list
nums =[1,2,3,4,5,5,6,7,8,8,9,1,10]
unique = list(set(nums))
print(unique)

#Max and Min in list
num=[10,5,25,8]
print(max(num), min(num))

#reverse a string
s="analytics"
print(s[::-1])

#Simple calculator
a =int(input("Enter first number: "))
b =int(input("Enter second number: "))
print("Sum: ", a+b)
print("Difference: ", a-b)
print("Product: ", a*b)