import re

def NegativeNumberInStrings(s):
    # Tìm tất cả các số âm trong chuỗi
    # Biểu thức chính quy: dấu '-' theo sau là 1 hoặc nhiều chữ số
    so_am = re.findall(r'-\d+', s)
    
    # In kết quả
    print("Các số nguyên âm trong chuỗi là:")
    for so in so_am:
        print(int(so))

# --- Chương trình chính ---
chuoi = input("Nhập vào một chuỗi: ")
NegativeNumberInStrings(chuoi)
