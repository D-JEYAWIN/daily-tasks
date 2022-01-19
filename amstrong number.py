num=int(input("enter the number: "))
l=len(str(num))
sum=0
a=num
while a>0:
     digit = a % 10
     sum += digit ** l
     a //= 10
if num == sum:
       print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")