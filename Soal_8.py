huruf = "SO"
e = 5
f = 5 
for i in range(e):
    for j in range(f-i):
        print(huruf[(i+j)%2], end=" ")
    print()
        
    