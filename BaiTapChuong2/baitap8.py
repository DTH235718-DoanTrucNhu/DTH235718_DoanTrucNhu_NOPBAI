# Các loại lỗi trong python
'''
1.Lỗi cú pháp(Syntax Error)
    -Xảy ra khi code viết sai cú pháp Python.
    -Chương trình không chạy được.

2.Lỗi thực thi (Runtime Error / Exception)
    -Xảy ra khi code đúng cú pháp nhưng gặp sự cố trong quá trình chạy.
    -Ví dụ: chia cho 0, truy cập phần tử không tồn tại, ép kiểu sai.

3.Lỗi logic (Logical Error)
    -Chương trình chạy không báo lỗi nhưng kết quả sai
    -Khó phát hiện hơn vì không có Exception.
'''
#Cách bắt lỗi trong python

# C1: Cú pháp cơ bản
try:
    # đoạn code có thể gây lỗi
    x = 10 / 0
except:
    # xử lý khi lỗi xảy ra
    print("Có lỗi xảy ra!")

#C2: Bắt lỗi cụ thể
try:
    x = int("abc")  # ép kiểu sai
except ValueError:
    print("Lỗi: Không thể chuyển chuỗi thành số nguyên")

#C3: Bắt nhiều loại lỗi
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Lỗi: Chia cho 0")
except ValueError:
    print("Lỗi: Sai giá trị")

#C4: Sử dụng else và finally
#else: chạy khi không có lỗi.
#finally: luôn chạy dù có lỗi hay không 
try:
    x = int(input("Nhập số nguyên: "))
except ValueError:
    print("Bạn phải nhập số!")
else:
    print("Bạn vừa nhập:", x)
finally:
    print("Kết thúc chương trình.")