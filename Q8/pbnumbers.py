number_frequency = {}
complementary_frequency = {}

with open('pbnumbers.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    numbers = list(map(int, line.strip().split()))
    for number in numbers[:-1]:
        if number in number_frequency:
            number_frequency[number] += 1
        else:
            number_frequency[number] = 1
    complementary_number = numbers[-1]
    if complementary_number in complementary_frequency:
        complementary_frequency[complementary_number] += 1
    else:
        complementary_frequency[complementary_number] = 1

# Sorting the dict by frequency
most_common = sorted(number_frequency.items(), key=lambda x: x[1], reverse=True)
least_common = sorted(number_frequency.items(), key=lambda x: x[1])

most_common_complementary = sorted(complementary_frequency.items(), key=lambda x: x[1], reverse=True)
least_common_complementary = sorted(complementary_frequency.items(), key=lambda x: x[1])

print("10 Most Common Numbers:")
for number, frequency in most_common[:10]:
    print(f"Number {number}: {frequency} times")

print("\n10 Least Common Numbers:")
for number, frequency in least_common[:10]:
    print(f"Number {number}: {frequency} times")

print("\n10 Most Common Complementary Numbers:")
for number, frequency in most_common_complementary[:10]:
    print(f"Complementary Number {number}: {frequency} times")

print("\n10 Least Common Complementary Numbers:")
for number, frequency in least_common_complementary[:10]:
    print(f"Complementary Number {number}: {frequency} times")
