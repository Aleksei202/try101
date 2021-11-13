import random

dice = random.randint(0, 50)

print(dice)
result = True

for i in range(0, 7):
    number = int(input('Enter number from 0 to 50\n'))
    if number > dice:
        print('The value is too high')
    elif number < dice:
        print('The value is too low')
    elif number == dice:
        result = False
        print('You guessed correctly!')
        break

if result:
    print(f'You fail, it was {dice}')
