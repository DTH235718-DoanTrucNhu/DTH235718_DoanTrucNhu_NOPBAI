import math

# Nhập n
n = int(input("Nhập n: "))

# Tính S(n)
S = 0
for i in range(n):
    S = math.sqrt(2 + S)

# Xuất kết quả
print("Giá trị S(n) =", S)
