def doc_so(n):
    # Danh sách các số đơn vị từ 0 đến 9
    don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    # Danh sách các số cho hàng chục từ 2 đến 9
    hang_chuc = ["", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]
    
    if n == 0:
        return "Không"
    
    if n < 10:
        return don_vi[n]
    elif n < 20:
        if n == 10:
            return "mười"
        else:
            return "mười " + don_vi[n % 10]
    else:
        chuc = n // 10
        don = n % 10
        if don == 0:
            return hang_chuc[chuc]
        else:
            return hang_chuc[chuc] + " " + don_vi[don]

# Nhập số và in ra kết quả
n = int(input("Nhập một số có tối đa 2 chữ số: "))
print(doc_so(n))