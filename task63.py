def is_even(user_inputs):
    for i in user_inputs:
        if i%2==0:
            print(i,'is even')
        else:
            print(i,'is odd')
user_inputs=[]
for i in range(3):
    nums=int(input('Enter number:'))
    user_inputs.append(nums)  
is_even(user_inputs)                  