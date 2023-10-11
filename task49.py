print('Lets play guessing game')
print('You get 5 attempt')
secret_number=46
max_attempt=5
for i in range(1,max_attempt+1):
    user_guess=int(input('Please guess number between 1 to 100:'))
    if user_guess>secret_number:
        print('Too high,try again')
    elif user_guess<secret_number:
        print('Too low,try again')
    else:
        print('Congratulation!You guess the secret number.You won the game')  
        break
else:
    print('You fail')          