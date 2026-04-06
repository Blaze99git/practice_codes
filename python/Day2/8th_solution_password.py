'''
8. Password Strength Checker
Problem: Check if a password is "Weak", "Medium", or "Strong". 
Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).
Also, check for the presence of uppercase letters, lowercase letters, digits, and special characters.
'''
def password_strength_checker(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    if length < 6:
        strength = "Weak"
    elif 6 <= length <= 10:
        strength = "Medium"
    else:
        strength = "Strong"

    criteria_met = sum([has_upper, has_lower, has_digit, has_special])

    return strength, criteria_met
# Example usage
password =input("Enter your password: ")
strength, criteria_met = password_strength_checker(password)
print(f"Password Strength: {strength}")
print(f"Criteria Met: {criteria_met} out of 4")
