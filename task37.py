month=input('Enter the month of year:')
if month =='January' or month=='February' or month=='March' or month=='April' or month=='May':
    print('Spring')
elif month=='June' or month=='July' or month=='August' :
    print('Summer')
elif month=='September' or month=='October' or month=='November':
    print('Fall')
elif month=='December':
    print('Winter')
else:
    print('Invalid month')               