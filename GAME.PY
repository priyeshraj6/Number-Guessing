import random
winning_num = random.randint(1,20)
trial = 1
max = 5

while True:
    if trial < max:
        try:
            n = int(input('Please enter a number between 1 and 20:'))
            if n == winning_num:
                print(f'congrats! you won in {trial} try')
                break
            elif n > winning_num:
                print(f"Too high,try again you have {max - trial-1} more chance")
                trial += 1
                continue
            else:
                print(f'too low,try again you have {max - trial-1} more chance')
                trial += 1
                continue
        except:
            print('only numbers are allowed,try again')
            continue
    else:
        print('Opps,limit exceeded')
        print(f'the winning number was {winning_num}.')
        pa = input('Do you want to play again?')
        response = ['yes', 'y']
        if pa.lower() in response:
            print('Great')
            trial = 1
            continue
        else:
            print('Good bye')
            break
