user_number=int(input('Enter number:'))
factorial=1
while user_number>0:
    factorial*=user_number
    user_number-=1
print('Factorial of number is ',factorial)    