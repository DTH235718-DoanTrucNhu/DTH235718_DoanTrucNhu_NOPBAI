# Bài tập 7: Trình bày một số cách nhập dữ liệu từ bàn phím.

#1.Nhập dữ liệu dạng chuỗi(string)
name=input("Nhập tên của bạn: ")
print("Xin chào!,", name)

#2.Nhập dữ liệu dạng số(int, float)
age = int(input("Nhập tuổi của bạn: "))   # Ép kiểu sang int
height = float(input("Nhập chiều cao (m): "))  # Ép kiểu sang float
print("Tuổi:", age)
print("Chiều cao:", height)

#3. Nhập nhiều giá trị trên cùng một dòng
a, b = input("Nhập 2 số cách nhau bởi khoảng trắng: ").split()
print("a =", a, ", b =", b)

#4.Nhập ký tự (chỉ lấy 1 ký tự)
char = input("Nhập 1 ký tự: ")[0]
print("Bạn vừa nhập:", char)

