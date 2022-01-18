from audioop import reverse


def reverse(string):
    string = "".join(reversed(string))
    return string

print("first name: ",end='')

first_name=str(input())
print("last name: ",end='')
last_name=str(input())
fname=reverse(first_name)
lname=reverse(last_name)
print("full name: ",end='')
print("{} {}".format(first_name,last_name))
print("reversed name: ",end='')
print("{} {}".format(fname,lname))

