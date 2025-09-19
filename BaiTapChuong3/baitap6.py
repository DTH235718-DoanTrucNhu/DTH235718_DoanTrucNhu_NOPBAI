def Docso(n):
    donvi = [" ","Một ","Hai ","Ba ","Bốn ","Năm ","Sáu ","Bảy ","Tám ","Chín "]
    if n<10:
        if n == 0:
            return "không"
        else:
            donvi[n]
    elif n<20:
        if n == 10:
            return "Mười"
        elif n == 15:
            return "Mười Lăm"
        else:
            return "Mười" + donvi[n%10]
    else: # 20->99
        chuc = n // 10
        dv = n% 10
        doc_chuc = donvi[chuc] + "Mươi"
        if dv == 0:
            return doc_chuc
        elif dv == 1:
            return donvi[chuc] + "Mốt"
        elif dv == 5:
            return donvi[chuc] + "Lăm"
        else:
            return donvi[chuc] +" "+ donvi[dv]
        
n =  int(input("Nhập số n ( 0 - 99): "))
if 0 <= n <= 99:
    print("Cách đọc: ", Docso(n))
else:
    print("Vui lòng nhập số từ 0 đến 99!")