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

print()
print()
print()

destination = input("Destination: ")
distance = float(input("Trip distance (miles): "))
mpg = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
people = int(input("Number of people splitting the cost: "))

gallons = distance / mpg
gas_cost = gallons * gas_price
cost_per_person = gas_cost / people
total_hours = distance / 55
hours = int(total_hours)
minutes = int((total_hours - hours) * 60)
round_trip_gas = gas_cost * 2

print()

print("-" * 3, f"Trip to {destination}", "-" * 3)
print(f"{'Gallons of gas:':<18}{gallons:.1f}")
print(f"{'Gas cost:':<18}${gas_cost:.2f}")
print(f"{'Cost per person:':<18}${cost_per_person:.2f}")
print(f"{'Driving time:':<18}{hours} hr {minutes} min (at 55 mph)")
print(f"{'Round trip gas:':<18}${round_trip_gas:.2f}")

print()
print()
print()

name = input("Employee name: ")
rate = float(input("Hourly pay rate: "))
hours = float(input("Hours worked this week: "))

# Calculations
gross_pay = hours * rate
fed_tax = gross_pay * 0.10
state_tax = gross_pay * 0.035
social_security = gross_pay * 0.062   # 6.2%
medicare = gross_pay * 0.0145         # 1.45%

total_deductions = fed_tax + state_tax + social_security + medicare
net_pay = gross_pay - total_deductions

keep_percent = (net_pay / gross_pay) * 100
yearly_gross = gross_pay * 52
yearly_net = net_pay * 52

# Output
print("\n" + "=" * 32)
print(f"PAY STUB: {name}")
print("=" * 32)
print(f"Hours worked:      {hours:.1f}")
print(f"Hourly rate:       ${rate:.2f}")
print(f"Gross pay:         ${gross_pay:.2f}")
print("-" * 32)
print(f"Federal tax (10%): ${fed_tax:.2f}")
print(f"State tax (3.5%):  ${state_tax:.2f}")
print(f"Social Security:   ${social_security:.2f}")
print(f"Medicare:          ${medicare:.2f}")
print(f"Total taken out:   ${total_deductions:.2f}")
print("-" * 32)
print(f"NET PAY:           ${net_pay:.2f}")
print("=" * 32)
print(f"You keep {keep_percent:.1f}% of what you earn.")
print(f"Yearly gross: ${yearly_gross:.2f}")
print(f"Yearly net:   ${yearly_net:.2f}")
