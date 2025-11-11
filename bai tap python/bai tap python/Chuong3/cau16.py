count = 0  # Đếm số lần in dấu '*'

for a in range(20, 100, 5):
    print('*', end='')  # In dấu '*' không xuống dòng
    count += 1  # Tăng số đếm sau mỗi lần in

print()  # Xuống dòng sau khi in tất cả dấu '*'
print(f"Số lượng dấu '*' được in ra là: {count}")