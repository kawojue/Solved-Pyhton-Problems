def get_monthly_costs():
    loan_payment = float(input("Enter the monthly loan payment: "))
    insurance = float(input("Enter the monthly insurance cost: "))
    gas = float(input("Enter the monthly gas cost: "))
    maintenance = float(input("Enter the monthly maintenance cost: "))
    return loan_payment, insurance, gas, maintenance


def calculate_total_monthly_costs(loan_payment, insurance, gas, maintenance):
    total_monthly_costs = loan_payment + insurance + gas + maintenance
    return total_monthly_costs


def calculate_total_annual_costs(total_monthly_costs):
    total_annual_costs = total_monthly_costs * 12
    return total_annual_costs


def main():
    print("Welcome to the Automobile Expense Calculator!")
    print("Please enter the monthly costs for the following expenses:")

    loan_payment, insurance, gas, maintenance = get_monthly_costs()
    total_monthly_costs = calculate_total_monthly_costs(loan_payment, insurance, gas, maintenance)
    total_annual_costs = calculate_total_annual_costs(total_monthly_costs)

    print("\nTotal Monthly Costs: ${:.2f}".format(total_monthly_costs))
    print("Total Annual Costs: ${:.2f}".format(total_annual_costs))


if __name__ == "__main__":
    main()
