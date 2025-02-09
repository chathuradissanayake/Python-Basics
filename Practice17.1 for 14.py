
pw = input("Enter your Password  ")       #qwertyy
letters = "ACNS"
numbers = ["1","5","6","9"]
crt = "*+&@"

for i in pw:
    for j in letters:
        if i is j:
            print(i,"ok")
            break
    for k in numbers:
        if i is k:
            print(i, "ok")
            break
    for l in crt:
        if i is l:
            print(i, "ok")
            break
else:
    print("Invalid Password")



#list = ["A","C","N","Z",1,5,6,9,"*","+","&","@"]