a = 5
b = 6

for i in range (a, 0, -1):
    for j in range (1, b, +1):
        if j < i :
            print("+", end=" ")
        else:
            print(j, end=" ")
    print( ) 