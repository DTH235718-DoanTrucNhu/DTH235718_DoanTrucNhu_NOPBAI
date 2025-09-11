# Tinh chu vi, dien tich hinh tron
import math

try:
    r = float(input("Mời bạn nhập bán kình hinh tròn: "))
    cv = 2*math.pi*r
    dt = r **2
    print("Chu vi = ", cv)
    print("Diện tích = ", dt)
except:    
    print("Lỗi rồi!")