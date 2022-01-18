import math
a=float(input("Enter the a value: "))
b=float(input("Enter the b value: "))
c=float(input("Enter the c value: "))
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the trainge : %0.2f"  %area)