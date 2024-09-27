balance = 999999
annualInterestRate = 0.18


lowerBound = balance / 12
monthlyInterestRate = annualInterestRate / 12
upperBound = balance * ((1 + monthlyInterestRate ) ** 12) / 12
originalBalance = balance
epsilon = 0.01 

while upperBound - lowerBound > epsilon:
    midpoint = (lowerBound + upperBound) / 2
    balance = originalBalance
    for month in range(12):
        unpaidBalance = balance - midpoint
        interest = unpaidBalance * monthlyInterestRate

        balance = unpaidBalance + interest
        # print(round(balance, 2))

    if balance > 0:
        lowerBound = midpoint
    else:
        upperBound = midpoint

print(round(midpoint, 2))