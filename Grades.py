#Marks input 90 > O 80 > a+,70>A


marks = float(input("Enter your marks: "))
grade = None

if(marks > 90 and marks <= 100):
    grade = "O"
elif(marks > 80 and marks <= 90):
    grade = "A"
elif(marks > 65 and marks <= 80):
    grade = "B"
elif(marks > 35 and marks <= 65):
    grade = "C"
elif (marks <= 35 and marks >= 0):
    grade= "F"
else:
    print("Invalid Input!")

print(f"Your griade is {grade}")