task = 0
working_hours = 0
wife_call = False

while working_hours < 8:
    print(f'Hour {working_hours + 1}')
    task += int(input('How many tasks will Maxim solve? '))
    working_hours += 1
    if int(input('Wife is calling. Answer? (1-yes, 0-no) ')) == 1:
        wife_call = True

print('Workday is over. Total tasks completed:', task)
if wife_call:
    print('Need to stop by the store')
