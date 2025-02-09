a=input("Enter your Choice ")

x=a[0]
y=int(a[1])


x1= ["a","b","c","d","e","f","g","h"]
y1= [1,2,3,4,5,6,7,8]

x2= ["a","c","e","g"]
y2= [1,3,5,7]

if (x in x1) and (y in y1):
    if (x in x2) and (y in y2):
        print(x, y, "= Black")
    else:
        print(x, y, "= White")

else:
    print(x,y,"Invalid Input")