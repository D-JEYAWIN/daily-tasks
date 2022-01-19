from random import choice

add = lambda x,y:x+y
sub = lambda x,y:x-y
mul = lambda x,y:x*y
div = lambda x,y:x/y
   
print("Simple calculator")
print("1. add","2. subtract","3. divison","4. multiplication")

choice = input("enter the choice: ")
if choice in ('1','2','3','4'):
    a=float(input("Enter the a value: "))
    b=float(input("enter the b value: "))

    if choice == '1':
        print("{} + {} = ".format(a,b),add(a,b))
    elif choice == '2':
        print("{} + {} = ".format(a,b),sub(a,b))
    elif choice == '3':
        print("{} + {} = ".format(a,b),mul(a,b))
    elif choice == '4':
        print("{} + {} = ".format(a,b),div(a,b))
else:
    print("invalid")
