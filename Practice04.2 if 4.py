name = input("Enter your name ")
fletter = name[0]
lletter = name[-1]
vowels = ["a","e","i","o","u"]

if (fletter in vowels) and (lletter in vowels):
    print("Both Lettrs")

elif fletter in vowels:
    print("First Letter")

elif lletter in vowels:
    print("Last Letter")

else:
    print("No Vowels")