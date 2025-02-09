name = input("Enter your name ")
fletter = name[0]
lletter = name[-1]

if (fletter== "a"or fletter=="e" or fletter=="i" or fletter=="o" or fletter=="u") and lletter=="a" or lletter=="e" or lletter=="i" or lletter=="o" or lletter=="u":
    print("Both Letters")

elif fletter== "a"or fletter=="e" or fletter=="i" or fletter=="o" or fletter=="u":
    print("First Letter")

elif lletter=="a" or lletter=="e" or lletter=="i" or lletter=="o" or lletter=="u":
    print("Last Letter")

else:
    print("No Vowel")

