square_feet = float(input("Enter the number of square feet of wall space to be painted: "))
paint_price = float(input("Enter the price of paint per gallon: $"))

gallons_required = square_feet / 112

paint_cost = gallons_required * paint_price

labor_hours = square_feet / 112

labor_cost = labor_hours * 25.00

total_cost = paint_cost + labor_cost

print(f"The number of gallons of paint required: {gallons_required:.2f} gallons")
print(f"The cost of the paint: ${paint_cost:.2f}")
print(f"The hours of labor required to complete the job: {labor_hours:.2f} hours")
print(f"The cost of the labor to complete the job: ${labor_cost:.2f}")
print(f"The total cost of the paint job: ${total_cost:.2f}")