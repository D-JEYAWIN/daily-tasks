numb=[]
n=int(input("enter the total number: "))
for i in range(0,n):
    number=int(input("enter the number: "))
    numb.append(number)

numb.sort()

print("number={}".format(numb))
print("sum =",sum(numb))
