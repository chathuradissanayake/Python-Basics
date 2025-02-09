x1 = 1
y1=[]
x2 = 1
y2=[]

a = int(input("පළමුසංඛ්‍යාව ඇතුලත් කරන්න "))
while a>=x1:
    z1=a%x1
    if z1==0:
        y1.append(x1)
        x1 += 1
    else:
        x1 += 1
print(a,"හිසාධක =",y1)


b = int(input("දෙවන සංඛ්‍යාව ඇතුලත් කරන්න "))
while b>=x2:
    z2=b%x2
    if z2==0:
        y2.append(x2)
        x2 += 1
    else:
        x2 += 1
print(b,"හිසාධක =",y2)

z = []
x = 0
while x<len(y1):
    if y1[x] in y2:
        z.append(y1[x])
        x += 1
    else:
        x +=1
print("පොදු සාධක =",z)

p = z[-1]
print("මහා පොදු සාධකය =",p)