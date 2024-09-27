# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# Process
# - Calculate the minimum payment
# - Calculate unpaid balance
# - Apply interest on unpaid balance
# - Calculate new balance for next month

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for month in range(12):
    # Minimum Monthly Payment
    # Minimum Payment = Current Balance × Minimum Payment Rate
    minimumPayment = balance * monthlyPaymentRate

    # Unpaid Balance After Minimum Payment
    # Unpaid Balance  = Current Balance − Minimum Payment
    unpaidBalance = balance - minimumPayment

    # Interest Calculation
    # Monthly Interest Rate = Annual Interest Rate / 12
    monthlyInterestRate = annualInterestRate / 12
    # Interest  =  Unpaid Balance × Monthly Interest Rate
    interest = unpaidBalance * monthlyInterestRate

    # New Balance for the Next Month
    # New Balance = Unpaid Balance + Interest
    balance = unpaidBalance + interest

print(round(balance, 2))


