n = int(input("Nhập chiều cao n: "))

# Hình 1: Hình vuông rỗng
print("Hình 1:")
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# Hình 2: Tam giác vuông
print("\nHình 2:")
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Hình 3: Hình chữ X
print("\nHình 3:")
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1 or i == 0 or i == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

