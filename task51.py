num1=int(input('Enter firt number:'))
num2=int(input('Enter second number:'))
total_sum=0
start_num=min(num1,num2)
end_num=max(num1,num2)
for num in range(start_num,end_num+1):
    total_sum+=num
print('Total sum of num1 and num2 is',total_sum)    