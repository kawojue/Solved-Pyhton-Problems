def calculate_packages(num_people, hotdogs_per_person):
    hotdogs_per_package = 10
    buns_per_package = 8

    total_hotdogs_needed = num_people * hotdogs_per_person
    hotdog_packages_needed = (total_hotdogs_needed + hotdogs_per_package - 1) // hotdogs_per_package

    total_buns_needed = num_people * hotdogs_per_person
    buns_packages_needed = (total_buns_needed + buns_per_package - 1) // buns_per_package

    hotdogs_leftover = (hotdog_packages_needed * hotdogs_per_package) - total_hotdogs_needed
    buns_leftover = (buns_packages_needed * buns_per_package) - total_buns_needed

    return hotdog_packages_needed, buns_packages_needed, hotdogs_leftover, buns_leftover


def main():
    try:
        num_people = int(input("Enter the number of people attending the cookout: "))
        hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

        hotdog_packages_needed, buns_packages_needed, hotdogs_leftover, buns_leftover = calculate_packages(num_people, hotdogs_per_person)

        print("\nMinimum number of packages of hot dogs required:", hotdog_packages_needed)
        print("Minimum number of packages of hot dog buns required:", buns_packages_needed)
        print("Number of hot dogs left over:", hotdogs_leftover)
        print("Number of hot dog buns left over:", buns_leftover)

    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
