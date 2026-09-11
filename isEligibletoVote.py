role = "STUDENT"
age = int(input("Enter your age: "))

isEligible = age < 21 and role.lower() == "student"

print("Eligible :",isEligible)
