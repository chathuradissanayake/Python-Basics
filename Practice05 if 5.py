x = int(input("Enter Number of Sides "))
if x>=3 and x<=8:
    if x == 3:
        print("Triangle")
    elif x == 4:
        print("Rectangle")
    elif x == 5:
        print("Pentagon")
    elif x == 6:
        print("Hexagon")
    elif x == 7:
        print("Heptagon")
    elif x == 8:
        print("Octagon")
else:
    print("Other")