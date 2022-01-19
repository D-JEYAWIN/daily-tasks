from tkinter import Y


def hcf_num(x, y):
    if x>y:
        small=Y
    else:
        small=x
    for i in range(1,small+1):
         if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf


num1=int(input("enter the value: "))
num2=int(input("enter the value: "))
print("the hcf value is",hcf_num(num1,num2))
    