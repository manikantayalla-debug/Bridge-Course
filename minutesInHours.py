minutes_Input = int(input("Enter the number of minutes: "))
hours = minutes_Input // 60
minutes = minutes_Input % 60
print(f"{minutes_Input} is {hours} hours {minutes} minutes")