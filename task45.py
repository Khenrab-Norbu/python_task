user_name=input('Enter your name:')
user_name=user_name.lower()
vowels={'a','e','i','o','u'}
number_of_vowels=0
for i in user_name:
    if i in vowels:
        number_of_vowels+=1
print('Total number of vowels ',number_of_vowels)        