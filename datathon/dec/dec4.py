#Selection Problem 4

acc_bal = int(input('Enter your account balance: '))
withdraw = int(input('Enter the amount to withdraw: '))

if withdraw < acc_bal:
    total = acc_bal - withdraw
    print('Balance is now', total)
else:
    print('Not enough balance')