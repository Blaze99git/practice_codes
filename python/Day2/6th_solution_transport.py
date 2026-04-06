'''
6. Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance 
(e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).
'''
def transportation_mode_selection(distance_km):
    if distance_km < 3:
        return "Walk"
    elif 3 <= distance_km <= 15:
        return "Bike"
    else:
        return "Car"
# Example usage
distance = int(input("Enter the distance in kilometers: "))
mode = transportation_mode_selection(distance)
print(f"Recommended mode of transportation: {mode}")