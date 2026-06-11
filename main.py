# Making a dictionary to ask the user about their basic info.
student_info = {
    "name" : input("Enter your name: "),
    "subjects" : {
        "Maths" : int(input("Enter marks of Maths: ")),
        "Stats" : int(input("Enter marks of Stats: ")),
        "English" : int(input("Enter marks of English: "))
    }
}
# Calculating total and percentage.
total = student_info["subjects"]["Maths"] + student_info["subjects"]["Stats"] + student_info["subjects"]["English"]
percentage = (total / 300) * 100

student_info["total"] = total
student_info["percentage"] = percentage

# Calculating grade
if percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
   grade = "C"
elif percentage >= 50:
   grade = "D"
else:
    grade = "Fail"

student_info["grade"] = grade

#Final report
print("\n-------Student Report-------")
print("Name:", student_info["name"])
print("Total:", student_info["total"])
print("Percentage:", student_info["percentage"])
print("Grade:", student_info["grade"])
