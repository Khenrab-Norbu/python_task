user_name=input('Enter your name:')
vowel={'a','e','i','o','u'}
user_name=user_name.lower()
contain_vowel=False
for i in user_name:
    if i in vowel:
        contain_vowel=True
print(contain_vowel)        
