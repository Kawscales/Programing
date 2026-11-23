name = input("Student name: ")
score = float(input("Score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
if grade == "A" or grade == "F":
    print(f"{name} got an {grade}.")
else:
    print(f"{name} got a {grade}.")
if score >= 60:
    print(f"{name} passed.")
else:
    print(f"{name} did not pass.")

print()
print()
print()

name=input("Name
