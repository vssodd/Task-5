# Simulate debt repayment until fully paid

debtor = input('Enter debtor name: ')
debt = int(input('Enter debt amount: '))
income = 0

while income < debt:
    income = int(input('How much money will you pay now to cover the debt? '))
    if income >= debt:
        print('Great,', debtor + ',', 'you have paid off the debt. Thank you!')
    else:
        print('Too little,', debtor + ',', 'please try again.')
