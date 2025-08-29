def ve_cay():

    la_cay = [1, 3, 7, 3, 5, 11]

    rong_nhat= 11
  
    for stars in la_cay:
        line = "*" * stars
        print(line.center(rong_nhat))

ve_cay()

def ve_than():
    cao = 2
    rong = 3
    for i in range(cao):
        line = " "
        for j in range(rong):
            if j == 0 or j == rong -1:
                line += "*"
            else:
                line += " "

        print(line.center(10))  

ve_than() 
