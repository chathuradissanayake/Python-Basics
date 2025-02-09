L = [1,2,3,4,5]
i = 0
while i< len(L):
    L[i] =L[i] + 1  #L[i] += 1
    i = i + 1       #i += 1
print(L)

t = "spam"
while t:    #x!=""
    print(t)
    t = t[1:]

y=10
while y:
    y = y-1
    if y%2 != 0:
        continue
    print(y)

z ="spam"
j=0
while j < len(z):
    print(z[j],end=" ")
    j += 1


b = 0

while b <= 2:
    x = 0
    print(b)
    while x <= 3:
        print(x)
        x += 1
    b += 1

m = True
n = False
o = True
p = 5
while m:
    while n:
        print("Dont Print")

    while p<10:
        print("Please Print")
        p +=1

