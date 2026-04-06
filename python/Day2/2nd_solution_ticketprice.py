'''
2. Movie Ticket Pricing
Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
'''
age_input = input("Enter your age: ")
age = int(age_input)
day_input = input("Enter the day of the week: ")
day = day_input.strip().lower()
ticket_price = 0
if day == "wednesday":
    if age < 18:
        ticket_price = 8 - 2
    else:
        ticket_price = 12 - 2
else:
    if age < 18:
        ticket_price = 8
    else:
        ticket_price = 12
print(f"Your ticket price is: ${ticket_price}")

