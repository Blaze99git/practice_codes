'''
4. Fruit Ripeness Checker
Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)
'''
def check_fruit_ripeness(fruit, color):
    ripeness_dict = {
        'Banana': {
            'Green': 'Unripe',
            'Yellow': 'Ripe',
            'Brown': 'Overripe'
        },
        'Apple': {
            'Green': 'Unripe',
            'Red': 'Ripe',
            'Brown': 'Overripe'
        },
        'Mango': {
            'Green': 'Unripe',
            'Yellow': 'Ripe',
            'Black': 'Overripe'
        }
    }
    
    fruit = fruit.capitalize()
    color = color.capitalize()
    
    if fruit in ripeness_dict:
        if color in ripeness_dict[fruit]:
            return ripeness_dict[fruit][color]
        else:
            return "Color not recognized for this fruit."
    else:
        return "Fruit not recognized."
    
# Example usage
fruit = input("Enter the fruit name (Banana, Apple, Mango): ")
color = input("Enter the color of the fruit: ")
ripeness = check_fruit_ripeness(fruit, color)
print(f"The {fruit} is {ripeness}.")