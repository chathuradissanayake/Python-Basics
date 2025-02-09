price = 0
total = 0
age =1
while age !=0:
    age = int(input("Enter your Age "))
    if age<= 2 and age >0:
        price = 0
        total = total + price   #total += price
    elif age >2 and age <= 12:
        price = 50
        total = total +price    #total += price
    elif age >= 65:
        price = 100
        total = total + price   #total += price
    elif age > 12 and age < 65:
        price = 150
        total += price   #total = total + price
    #else:
        #continue

print("Total price = Rs", total)


