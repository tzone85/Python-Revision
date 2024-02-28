# get details of the loan

money_owed = float(input('How much money do you owe, in dollars?\n')) # $9000
annual_percentage_rate = float(input('What is the annual percentage rate?\n')) # 3.7
monthly_payment = float(input('What will your monthly payment be, in dollars?\n')) # $100
months = int(input('How many months do you want to see the results for?\n')) # 6

monthly_interest_rate = annual_percentage_rate / 12 / 100

for i in range(months):

    # calculate interest to pay
    interest_paid = money_owed * monthly_interest_rate

    # add interest
    money_owed = money_owed + interest_paid

    if (money_owed - monthly_payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break 

    # make payment
    money_owed = money_owed - monthly_payment

print('Paid', monthly_payment, 'of which', interest_paid, 'was interest.')
print('Now I owe', money_owed)
