print('Think of a number between 1 and 100 and write it down.')

min_num = 1
max_num = 100

print('')

while True:
    guess = (min_num + max_num) // 2
    print(f'Is your number equal to, greater than, or less than {guess}?')
    user_input = input('Enter 1 (=), 2 (>), 3 (<): ')
    
    if user_input == '1':
        print(f'Hooray! I guessed it! Your number is {guess}.')
        break
    elif user_input == '2':
        min_num = guess + 1
    elif user_input == '3':
        max_num = guess - 1
