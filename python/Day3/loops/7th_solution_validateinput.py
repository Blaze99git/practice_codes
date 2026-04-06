'''
7. Validate Input
Problem: Keep asking the user for input until they enter a number between 1 and 10.
'''
while True:
    user_input = input("Please enter a number between 1 and 10: ")
    try:
        number = int(user_input)
        if 1 <= number <= 10:
            print(f"Thank you! You entered a valid number: {number}")
            break
        else:
            print("The number is out of range. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")