rows=int(input("enter the no.of rows: "))
cols=int(input("enter the no.of column: "))
l=[]
for i in range(rows):
    col=[]
    for j in range(cols):
        col.append(int(input("enter the value :")))
    l.append(col)

    print(l)