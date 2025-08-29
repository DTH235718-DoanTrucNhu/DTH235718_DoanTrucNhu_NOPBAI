
cao = 4
rong =4
for i in range(cao):
    for j in range(rong):
      
        if i == 0 or i == cao - 1 or j == 0 or j == rong - 1:
            print("*", end="")
        else:
            print(" ", end="")  
    print() 