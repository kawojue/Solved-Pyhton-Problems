from os import path, getcwd


def read_steps_file(file_path):
    with open(file_path, 'r') as file:
        steps_data = file.readlines()
    return [int(steps.strip()) for steps in steps_data]


def calculate_monthly_averages(steps_data):
    months = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31,
    }

    monthly_averages = {}
    month_data = []
    current_month = None

    for day, steps in enumerate(steps_data, 1):
        if day == 1:
            current_month = 'January'
        elif day == 32:
            current_month = 'February'
        elif day == 60:
            current_month = 'March'
        elif day == 91:
            current_month = 'April'
        elif day == 121:
            current_month = 'May'
        elif day == 152:
            current_month = 'June'
        elif day == 182:
            current_month = 'July'
        elif day == 213:
            current_month = 'August'
        elif day == 244:
            current_month = 'September'
        elif day == 274:
            current_month = 'October'
        elif day == 305:
            current_month = 'November'
        elif day == 335:
            current_month = 'December'

        if current_month not in monthly_averages:
            monthly_averages[current_month] = 0

        monthly_averages[current_month] += steps
        month_data.append(steps)

        if day == months[current_month]:
            monthly_averages[current_month] /= months[current_month]
            month_data.clear()

    return monthly_averages


def count_days_with_10000_or_more(steps_data):
    return sum(1 for steps in steps_data if steps >= 10000)


def main():
    # Steps data from the provided file
    file_path = path.join(getcwd(), "Steps.txt")
    steps_data = read_steps_file(file_path)

    monthly_averages = calculate_monthly_averages(steps_data)
    for month, average_steps in monthly_averages.items():
        print(f"{month}: {average_steps:.2f} steps")

    days_with_10000_or_more = count_days_with_10000_or_more(steps_data)
    print(f"Number of days with 10000 or more steps: {days_with_10000_or_more}")


if __name__ == "__main__":
    main()
