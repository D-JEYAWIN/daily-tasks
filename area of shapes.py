import math
m=float(input("Enter the m value: "))
n=float(input("Enter the n value: "))
o=float(input("Enter the o value: "))
# area of triangle
s = (m+n+o)/2
area = (s*(s-m)*(s-n)*(s-o))**0.5
print("Area of the trainge : %0.2f"  %area)

print("------------------------------------------")
print("------------------------------------------")
l=float(input("Enter the length value: "))
b=float(input("Enter the breadth value: "))
# area of rectangle
area_rect=l*b
print("Area of the rectangle : %0.2f"  %area_rect)

print("------------------------------------------")
print("------------------------------------------")
h=float(input("Enter the height value: "))
# area of parallelogram
area_para=b*h
print("Area of the prllelogram : %0.2f"  %area_para)
print("------------------------------------------")
print("------------------------------------------")
a=float(input("Enter the area value: "))

#area of square
area_square= a**a
print("Area of the square : %0.2f"  %area_square)








