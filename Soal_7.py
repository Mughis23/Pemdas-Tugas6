huruf = "AB"
c = 4
d = 5 
for i in range(c):
    for j in range(d):
        print(huruf[(i+j)%2], end=" ")
    print()        
        