'''7. Coffee Customization
Problem: Customize a coffee order: "Small", "Medium", or "Large" 
with an option for "Extra shot" of espresso.'''

def coffee_customization(size, extra_shot):
    sizes = ["Small", "Medium", "Large"]
    if size not in sizes:
        return "Invalid size selected."

    order = f"Coffee Size: {size}"
    if extra_shot:
        order += " with Extra Shot of Espresso"
    else:
        order += " without Extra Shot"

    return order
# Example usage:
input_size = input("Enter coffee size (Small/Medium/Large): ")
input_extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").strip().lower() == 'yes'
print(coffee_customization(input_size, input_extra_shot))
