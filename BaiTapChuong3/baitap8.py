import math
print("Tính + - * / của a,b ")


def Cong(a,b):
    return a + b

def Tru(a,b):
    return a - b

def Nhan(a,b):
    return a * b

def Chia(a,b):
    if b == 0:
        return "Không thể chia 0"
    return a / b

def Phep_tinh():
    try:
        a = float(input("Nhập số a: "))
        b = float(input("Nhập số b:"))
        phep_toan = input("Chọn phép toán (+ - * /) :")
        
        if phep_toan == "+":
            print(f"Kết quả: {a} + {b} = {Cong(a,b)}")
        elif phep_toan == "-":
            print(f"Kết quả: {a} - {b} = {Tru(a,b)}")
        elif phep_toan == "*":
            print(f"Kết quả: {a} * {b} = {Nhan(a,b)}")
        else:
            print(f"Kết quả: {a} / {b} = {Chia(a,b)}")
    except ValueError:
                print("Ngày tháng năm không hơp lệ vui lòng nhập lại!")

Phep_tinh()