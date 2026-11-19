customer_name = input("Customer name: ")
item = input("Item: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
tax = subtotal * 0.07
total = subtotal + tax

print()

print(f"--- Receipt for {customer_name} ---")
print(f"Item:      {item}")
print(f"Quantity:  {quantity}")
print(f"Subtotal:  ${subtotal:.2f}")
print(f"Tax (7%):  ${tax:.2f}")
print(f"Total:     ${total:.2f}")

print()
print()

print("Host name: Jordan")
print("Number of people: 10")
print("Slices per person: 3")

print()

print("=== Pizza Plan for Jordan's Party ===")
print("Slices needed:    30")
print("Whole pizzas:     3")
print("Extra slices:     6")
print("Total cost:       $52.47")
print("Cost per person:  $5.25")

print()
print()

import math

host = input("Host name: ")
people = int(input("Number of people: "))
slices_per_person = int(input("Slices per person: "))

slices_needed = people * slices_per_person
whole_pizzas = math.ceil(slices_needed / 16)
extra_slices = (whole_pizzas * 16) - slices_needed
total_cost = whole_pizzas * 21.99
cost_per_person = total_cost / people

print()

print(f"=== Pizza Plan for {host}'s Party ===")
print(f"Slices needed:    {slices_needed}")
print(f"Whole pizzas:     {whole_pizzas}")
print(f"Extra slices:     {extra_slices}")
print(f"Total cost:       ${total_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")


