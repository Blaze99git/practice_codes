'''
5. Weather Activity Suggestion
Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
'''
def suggest_activity(weather):
    weather = weather.lower()
    if weather == 'sunny':
        return "It's a great day to go for a walk!"
    elif weather == 'rainy':
        return "Perfect time to read a book indoors."
    elif weather == 'snowy':
        return "How about building a snowman?"
    else:
        return "I dont know how about you decide!"
# Example usage
weather_condition = input("Enter the weather condition (Sunny, Rainy, Snowy): ")
activity = suggest_activity(weather_condition)
print(activity)