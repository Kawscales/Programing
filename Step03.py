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

print(f"{name} got a {grade}.")

if score >= 60:
    print(f"{name} passed.")
else:
    print(f"{name} did not pass.")

print()
print()
print()

name = input("Name: ")
age = int(input("Age: "))
day = input("Day of the week: ").strip()
is_3d = input("3D movie? (y/n): ").strip().lower()


if age < 13:
    ticket_type = "Child"
    base_price = 7.00
elif age >= 65:
    ticket_type = "Senior"
    base_price = 8.00
else:
    ticket_type = "Adult"
    base_price = 11.00

total = base_price


if day.lower() == "tuesday":
    total -= 2.00


if is_3d == "y":
    total += 3.00

print()
print("-" * 3, f"Ticket for {name}", "-" * 3)
print(f"{'Ticket type:':<15}{ticket_type}")
print(f"{'Base price:':<15}${base_price:.2f}")
print(f"{'Total:':<15}${total:.2f}")

print()
print()
print()

order_total = float(input("Order total: "))
weight = float(input("Package weight (lbs): "))
zone = int(input("Shipping zone (1-3): "))
rush = input("Rush delivery? (y/n): ").strip().lower()

if zone == 1:
    shipping = 3.00
    days = 2
elif zone == 2:
    shipping = 4.50
    days = 4
else:
    shipping = 6.00
    days = 6

if rush == "y":
    shipping += 5.00
    days = max(1, days - 2)

grand_total = order_total + shipping

print()
print("-" * 3, "Shipping Summary", "-" * 3)
print(f"{'Order total:':<14}${order_total:.2f}")
print(f"{'Shipping:':<14}${shipping:.2f}")
print(f"{'Grand total:':<14}${grand_total:.2f}")
print(f"{'Arrives in:':<14}{days} days")

print()
print()
print()

name = input("Member name: ")
grade = int(input("Grade (9-12): "))
gpa = float(input("GPA (0.0-4.0): "))
dues = input("Dues paid? (y/n): ").strip().lower()
events = int(input("Events signed up for: "))

print()
print("-" * 3, f"BPA Check for {name}", "-" * 3)

if dues == "y" and gpa >= 2.0 and events >= 1:
    print("Status: ELIGIBLE")

    if events == 1:
        print("You are entered in 1 event.")
    else:
        print(f"You are entered in {events} events.")
    if grade >= 10 and gpa >= 3.0:
        print("You can run for chapter office.")
    else:
        print("You cannot run for chapter office.")
else:
    print("Status: NOT ELIGIBLE")
