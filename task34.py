temperature=int(input('Temperature:'))
if temperature>=100:
    print('Boiling')
elif temperature >=32 and temperature<100:
    print('Liquid')
else :
    print('Frezing')      