HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

num_people = int(input("Enter the number of people attending the cookout: "))
hotdogs_per_person = int(input("Enter the number of hot dogs each person will be given: "))

print()

total_hotdogs_needed = num_people * hotdogs_per_person
total_buns_needed = total_hotdogs_needed // HOT_DOGS_PER_PACKAGE * BUNS_PER_PACKAGE

hotdogs_leftover = total_hotdogs_needed % HOT_DOGS_PER_PACKAGE
buns_leftover = total_buns_needed % BUNS_PER_PACKAGE

packages_hotdogs_required = total_hotdogs_needed // HOT_DOGS_PER_PACKAGE
packages_buns_required = total_buns_needed // BUNS_PER_PACKAGE

print("Minimum number of packages of hot dogs required: ", packages_hotdogs_required)
print("Minimum number of packages of hot dog buns required: ", packages_buns_required)
print("Number of hot dogs left over: ", hotdogs_leftover)
print("Number of hot dog buns left over: ", buns_leftover)
