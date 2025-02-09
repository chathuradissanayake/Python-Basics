x = 0
while x<=50:
    print(x)   #counting up while loops
    x += 1


x1 = 0
while x1<=100:
    if x1%3==0 and x1%5==0:
        print(x1)
        x1=x1 + 1
    else:
        x1 = x1 + 1


x2 = input("Enter Your Name ")
y2 = 0
while y2< len(x2):
    print(x2[y2])
    y2 += 1