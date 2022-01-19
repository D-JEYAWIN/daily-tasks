print("enter the year:",end='')
year=int(input())
if (year%400==0) and (year%100==0):
    print('{} is an leap year'.format(year))
elif (year%4==0) and (year%100!=0):
    print('{} is an leap year'.format(year))
else:
    print('{} is not an leap year'.format(year))
    
          