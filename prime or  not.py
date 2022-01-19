import math
n=int(input("enter the value: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("{} is not an prime number".format(n))
            
            break
        else:
            print("{} is an prime number".format(n))
            break
else:
    print("{} it ia not an proper number".format(0))