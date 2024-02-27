
expenses = []
total = 0
for i in range(7):
    expenses.append(float(input("Enter an expense: ")))

total = sum(expenses)
# print("You spent $" + str(sum) + " this week.", sep="")
print("You spent $", total, " this week.", sep="")