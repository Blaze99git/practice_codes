'''
9. Leap Year Checker
Problem: Determine if a year is a leap year. (Leap years are divisible by 4, 
but not by 100 unless also divisible by 400).
'''
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
# Example usage:
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")    
