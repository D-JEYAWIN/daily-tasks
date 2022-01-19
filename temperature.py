import math
fahren=float(input("Enter the fahrenheit tempertaure: "))
celsius=float(input("Enter the celsius tempertaure: "))
kelvin=float(input("Enter the kelvin tempertaure: "))
print(" ")
# fahrenhiet to celsius
f2c=((fahren - 32) * (5/9))
print("{} farenheit is {} celsius".format(fahren,f2c))
print(" ")
# fahrenhiet to kelvin
f2k=((fahren - 32) * (5/9) + 273.15)
print("{} farenheit is {} kelvin".format(fahren,f2k))
print(" ")
# celsius to fahrenhiet 
c2f=((celsius * 9/5) + 32 )
print("{} celsius is {} farenheit".format(celsius,c2f))
print(" ")
# celsius to kelvin
c2k=(celsius + 273.15)
print("{} celsius is {} kelvin".format(celsius,c2k))
print(" ")
# kelvin to fahrenhiet 
k2f=((kelvin * 273.15) * (9/5) + 32)
print("{} kelvin is {} farenheit".format(kelvin,k2f))
print(" ")
# kelvin to celsius
k2c=(kelvin - 273.15)
print("{} kelvin is {} celsius".format(kelvin,k2c))

    
