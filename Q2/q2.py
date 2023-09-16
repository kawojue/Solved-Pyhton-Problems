loan_payment = float(input("Enter your monthly loan payment: $"))
insurance = float(input("Enter your monthly insurance cost: $"))
gas = float(input("Enter your monthly gas cost: $"))
maintenance = float(input("Enter your monthly maintenance cost: $"))

total_monthly_costs = loan_payment + insurance + gas + maintenance
total_annual_costs = total_monthly_costs * 12

print("\nTotal Monthly Expenses: $", total_monthly_costs)
print("Total Annual Expenses: $", total_annual_costs)
