import matplotlib.pyplot as plt

expenses_data = {}

with open("expenses.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line:
            category, amount = line.split("=")
            expenses_data[category.strip()] = float(amount)

categories = list(expenses_data.keys())
amounts = list(expenses_data.values())

plt.figure(figsize=(7, 7))
plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=120)
plt.title("Monthly Expenses Distribution")
plt.axis('equal')

plt.show()
