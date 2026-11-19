total = 11.00

day = input("Day: ")
three_d = input("3D? (y/n) : ")
popcron_d=input("PopCorn(y/n): ")

if day.lower() == "tuesday":
    total = total - 3.00
if three_d.lower() == "y":
    total = total + 2.50
if popcorn.lower() =="y":
    total = total +3.50
print(f"Total: ${total:.2f}")
