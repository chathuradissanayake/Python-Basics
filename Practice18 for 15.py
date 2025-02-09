binary = input("Enter the Binary Number ")
y = len(binary)
num = 0

for i in binary:
        if i == "1":
            z=2**(y-1)
            num = num + z
            y=y-1
        elif i == "0":
            y=y-1
            continue
        else:
            print("Invalid Input")
            break
print(num)