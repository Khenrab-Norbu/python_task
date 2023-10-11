num1=int(input('Enter the first number:'))
num2=int(input('Enter the second  number:'))
total_sum=0
if num1<=num2:
    current_num=num1
    while current_num<=num2:
        total_sum+=current_num
        current_num+=1
else:
    current_num=num2
    while current_num<=num1:
        total_sum+=current_num
        current_num+=1
print('Total sum of num1 and num2 is',total_sum)              
