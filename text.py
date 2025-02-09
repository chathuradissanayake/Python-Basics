total = 0
a = input("Enter Number ")
for i in a:
    b = int(i)
    total += b
print(total)


def num_total(a):
    total = 0
    #a = input("Enter Number ")
    for i in a:
        b = int(i)
        total += b
    print(total)
num_total(1234)


binary = input("Enter the Binary Number ")
y = len(binary)
x=0
num = 0
i = int(binary[x])
print(i)
while x < y:
        if i == 1:
            z=2**(y-1)
            num = num + z
            y=y-1
            x += 1
            continue
        elif i == 0:
            y=y-1
            x+= 1
            continue
        else:
            print("Invalid Input")
            break

print(num)