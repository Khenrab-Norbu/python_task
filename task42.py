user_name=input('Enter your Name :')
user_name=user_name.lower()
vowel={'a','e','i','o','u'}
contain_vowel=False
x=0
while len(user_name)>x:
    if user_name[x] in vowel:
        contain_vowel=True
    x+=1            
print(contain_vowel)
