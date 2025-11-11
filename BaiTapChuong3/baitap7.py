import datetime 
def Nhap_ngaythangnam():
      while True:
            try:
                ngay = int(input("Nhập ngày: "))
                thang = int(input("Nhập tháng: "))               
                nam = int(input("Nhập năm: "))
                datetime.date(nam, thang, ngay)
                return ngay, thang, nam
            except ValueError:
                print("Ngày tháng năm không hơp lệ vui lòng nhập lại!")
              
def Nam_nhuan(nam):
     return (nam% 400 == 0) or (nam % 4 == 0 and nam % 100 != 0)

def Ngay_tiep_theo(ngay,thang,nam):
    if Nam_nhuan(nam):
            ngay_trong_thang = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
            ngay_trong_thang = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    ngay += 1
    if ngay > ngay_trong_thang[thang - 1]:
        ngay = 1
        thang += 1
        if thang > 12:
              thang =1
              nam += 1
    return ngay, thang, nam
        
print("Chương trình tìm ngày tiếp theo.")
ngay, thang, nam = Nhap_ngaythangnam()
ngay_moi, thang_moi, nam_moi = Ngay_tiep_theo(ngay, thang, nam)
print(f"Ngày tiếp theo là: {ngay_moi}/{thang_moi}/{nam_moi}")