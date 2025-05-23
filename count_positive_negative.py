positive_count = 0
negative_count = 0

number = int(input('Enter a number: '))

while number != 0:
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    number = int(input('Enter a number: '))

print('Count of positive numbers:', positive_count)
print('Count of negative numbers:', negative_count)
