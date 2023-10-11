user_name=input('Enter your name :')
user_name=user_name.lower()
vowels={'a','e','i','o','u'}
number_of_vowels=0
i=0
while len(user_name)>i:
    if user_name[i] in vowels:
        number_of_vowels+=1
    i+=1    
print('Total number of vowels are ',number_of_vowels)   
