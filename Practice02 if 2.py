x= int(input("Enter the Date "))
y = input("Enter Month ")
print(y,x)
if x==1 and (y=="january" or y=="july"):
    print("Holiday")
elif x==25 and y=="december":
    print("Holyday")
else:
    print("Working Day")