x = -2
y = 2
while x <= y:
    print("x is now ",x)
    x += 1   #x=x+1
    while x <= 0:
        print("x is Negative")
        x += 1   #x=x+1


matrix = [[5,4,7,11],[3,3,8,17]]
i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        print(matrix[i][j])
        j = j + 1
    i= i + 1


i = 0
m = 2
while i < m:
    j = 0
    n = 2
    while j<n:
        j = j+1
        print("j is = ", j)
    i = i + 1
    print("i is =", i)