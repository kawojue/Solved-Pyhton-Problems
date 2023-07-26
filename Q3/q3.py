def main():
    # Get user input
    square_feet = int(input("Enter the number of square feet of wall space to be painted: "))
    paint_price_per_gallon = float(input("Enter the price of paint per gallon: "))

    # Calculate the number of gallons of paint required
    gallons_required = square_feet / 112

    # Calculate the cost of the paint
    paint_cost = gallons_required * paint_price_per_gallon

    # Calculate the hours of labor required to complete the job
    hours_of_labor = square_feet / 112

    # Calculate the cost of labor to complete the job
    labor_cost = hours_of_labor * 25.00

    # Calculate the total cost of the paint job
    total_cost = paint_cost + labor_cost

    # Display the results
    print(f"\nNumber of gallons of paint required: {gallons_required:.2f}")
    print(f"Cost of paint: ${paint_cost:.2f}")
    print(f"Hours of labor required: {hours_of_labor:.2f}")
    print(f"Cost of labor: ${labor_cost:.2f}")
    print(f"Total cost of the paint job: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
