balance = 3926
annualInterestRate = 0.2
minimumPayment = 0
originalBalance = balance

while balance > 1:
    minimumPayment += 10
    balance = originalBalance
    for month in range(12):
        unpaidBalance = balance - minimumPayment

        monthlyInterestRate = annualInterestRate / 12
        interest = unpaidBalance * monthlyInterestRate

        balance = unpaidBalance + interest
        # print(round(balance, 2))

print(minimumPayment)