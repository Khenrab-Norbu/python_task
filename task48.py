print('Lets play gussing game')
#user_guess=int(input('Guess a number from 1 to 100 :'))
secret_number=46
while True:
    user_guess=int(input('Guess a number from 1 to 100 :'))
    if user_guess > secret_number:
        print('Too high,try again')
    elif user_guess<secret_number:
        print('Too low, try again')   
    else:
        print('Congratulation! You won.You guess the secret number which is ',secret_number)         
        break