number = int(input('Enter the target number: '))
count = 0

while number > 0:
    guess_number = int(input('Guess the number: '))
    count += 1
    if guess_number < number:
        print('The number is smaller than needed. Try again!')
    elif guess_number > number:
        print('The number is larger than needed. Try again!')
    else:
        print('You guessed it! Number of attempts:', count)
        break
