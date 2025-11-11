import math

# Nhập x và n
x = float(input("Nhập giá trị x: "))
n = int(input("Nhập giá trị n: "))

S = 0
for i in range(n+1):
    S += x**(2*i+1) / math.factorial(2*i+1)

print("Giá trị S(x, n) =", S)
