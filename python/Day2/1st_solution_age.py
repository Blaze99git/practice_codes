'''1. Age Group Categorization
Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).'''

ageinput=input("Enter the age: ")
ageinint=int(ageinput)

if(ageinint<13):
    print ("Child")
elif ageinint >= 13 and ageinint<20:
    print ("Teenager")
elif ageinint >= 20 and ageinint<60:
    print ("Adult")
else:
    print ("Senior")
