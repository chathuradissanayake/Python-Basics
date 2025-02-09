x= int(input("Enter the Price "))
y= x%5

if y==0 or y==1 or y==2:
    print("Rs",x-y)
elif y==3 or y==4:
    print("Rs",x-y+5)

else:
    print("Enter currect Price ")