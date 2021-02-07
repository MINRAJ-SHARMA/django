x=input('please enter a year')
year=int(x)
if((year%400==0)or((year%4==0)and(year%100!=0))):
    print('leap year')

else:
    print('not leap year') 
