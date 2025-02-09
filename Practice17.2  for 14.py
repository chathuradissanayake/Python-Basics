list = ["A","C","N","Z","1","5","6","9","*","+","&","@"]

pw = input("Enter your Password ")

for i in pw:
    if i in list:
        print(i,"Correct")
        continue
    else:
        #print(i,"Wrong")
        continue