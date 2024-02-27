
expenses = []
total = 0
num_expenses = int(input("How many expenses do you have? "))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)
# print("You spent $" + str(sum) + " this week.", sep="")
print("You spent $", total, " this week.", sep="")