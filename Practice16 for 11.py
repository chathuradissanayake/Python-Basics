for i in range(1,101):
    if i%5==0 and i%7==0:
        print(i)

print("\n")

total = 0
for j in range(1,101):
    total += j
print(total)

print("\n")

for k in range(2,101):
    for l in range (2,k):
        if k%l==0:
            break
    else:
        print(k)