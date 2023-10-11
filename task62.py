def is_even(user_input):
    
    for i in user_input:
        if i%2!=0:
            return False
    return True

user_input=[]
for i in range(3):
    num=int(input('Enter number:'))
    user_input.append(num)
result=is_even(user_input) 
if result:
    print('True')               
else:
    print('False')
