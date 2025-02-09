Celcious1 = float(input("Enter Heat in Celcious = "))
Faronhite1 = Celcious1 * 9/5 + 32
print(Faronhite1,"F")

Faronhite2 = float(input("Enter Heat in Faronhite = "))
Celcious2 = (Faronhite2 -32) * 5/9
print(Celcious2,"C")

Heat = float(input("Enter Temperrature "))
Unit = input("Enter Unit, Enter C if Celcious , Enter F if Faronhite ")
if Unit=="C":
    Temperature1 = Heat * 9 / 5 + 32
    print("Temperature in Faronhite is ",Temperature1,"F")
elif Unit=="F":
    Temperature2 = (Heat - 32) * 5 / 9
    print("Temperature in Celcious is ", Temperature2, "C")
else:
    print("Invalid Units")