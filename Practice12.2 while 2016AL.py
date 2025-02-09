manu = {1:10.00,2:12.00,3:15.00,4:10.00,5:25.00,6:45.00,7:50.00,8:25.00,9:10.00,10:12.00}
item = 1
price = 0
total = 0
while item >0:
    item=int(input("Enter Item Number "))
    if item >0:
        quantity = int(input("Enter Quantity "))
        price = manu[item] * quantity
        total = total + price
        continue
    else:
        break

print("Total Price",total)
