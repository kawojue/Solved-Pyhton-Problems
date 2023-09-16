from os import path, getcwd

monthly_steps = [0] * 12
days_with_10000_or_more_steps = 0
file_path = path.join(getcwd(), "Steps.txt")

with open(file_path, "r") as file:
    lines = file.readlines()

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, steps_str in enumerate(lines):
    steps = int(steps_str.strip())
    
    month = i % 12
    
    monthly_steps[month] += steps
    
    if steps >= 10000:
        days_with_10000_or_more_steps += 1

for i in range(12):
    average_steps = monthly_steps[i] / days_in_month[i]
    print(f"Average steps for Month {i + 1}: {average_steps:.2f}")

print(f"Total days with 10000 or more steps: {days_with_10000_or_more_steps}")