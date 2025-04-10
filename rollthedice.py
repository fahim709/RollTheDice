import random
while True:
    user = input('Roll the  Dice?(YES/NO): ').upper()
    if user == 'YES':
         a = random.randint(1, 50)
         b = random.randint(1, 50)
         print(f'({a} {b})')
    elif user == 'NO':
        print('Thanks for playing')
        break
    else:
        print('Invalid Choice')

