x=1
y=1
number= int(input("Enter Number "))

if number>1:
    y = number * (number - x)
    while number>x+1:
        x = x + 1
        y = y*(number-x)
        continue
    print("Factorial is",y)
else:
    print("Factorial is",y)