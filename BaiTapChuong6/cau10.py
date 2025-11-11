def get_matrix_dimensions():
    """Hàm nhập kích thước (hàng và cột) cho ma trận."""
    while True:
        try:
            rows = int(input("Nhập số hàng (m): "))
            cols = int(input("Nhập số cột (n): "))
            if rows > 0 and cols > 0:
                return rows, cols
            else:
                print("Số hàng và số cột phải là số nguyên dương.")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

def input_matrix(name, rows, cols):
    """Hàm nhập các phần tử cho ma trận dưới dạng list lồng nhau."""
    print(f"\n--- Nhập ma trận {name} ({rows}x{cols}) ---")
    matrix = []
    
    for i in range(rows):
        row = [] # List cho hàng thứ i
        for j in range(cols):
            while True:
                try:
                    element = float(input(f"Nhập phần tử {name}[{i}][{j}]: "))
                    row.append(element)
                    break
                except ValueError:
                    print("Đầu vào không hợp lệ. Vui lòng nhập một số thực.")
        matrix.append(row)
            
    return matrix

def print_matrix(name, matrix):
    """Hàm in ma trận ra màn hình một cách dễ đọc."""
    print(f"Ma trận {name}:")
    for row in matrix:
        print(row)
def add_matrices(A, B, rows, cols):
    """Thực hiện phép cộng ma trận C = A + B."""
    C = []
    for i in range(rows):
        row = []
        for j in range(cols):
            # Thực hiện phép cộng từng phần tử
            sum_element = A[i][j] + B[i][j]
            row.append(sum_element)
        C.append(row)
    return C
def transpose_matrix(matrix, original_rows, original_cols):
    """Hàm tính ma trận chuyển vị (A^T)."""
    transposed = []
    
    # Kích thước ma trận chuyển vị là original_cols x original_rows
    for j in range(original_cols): # Lặp qua CỘT của ma trận gốc (để trở thành HÀNG mới)
        new_row = []
        for i in range(original_rows): # Lặp qua HÀNG của ma trận gốc
            # Lấy phần tử A[i][j] và đặt vào vị trí mới [j][i]
            new_row.append(matrix[i][j])
        transposed.append(new_row)
        
    return transposed
print("==================================================")
print("CHƯƠNG TRÌNH XỬ LÝ MA TRẬN BẰNG PYTHON LISTS")

# 1. Nhập kích thước chung cho A và B
print("\n[Bước 1: Nhập kích thước ma trận]")
m, n = get_matrix_dimensions()

# 2. Nhập Ma trận A và B
A = input_matrix("A", m, n)
B = input_matrix("B", m, n)

print("\n--- MA TRẬN ĐẦU VÀO ---")
print_matrix("A", A)
print_matrix("B", B)
print("-----------------------")

# 3. Cộng 2 ma trận (A + B)
print("\n[Bước 2: Cộng hai ma trận A + B]")
C = add_matrices(A, B, m, n)
print_matrix("C = A + B", C)
print("-----------------------")

# 4. Tính ma trận chuyển vị (hoán vị) cho A và B
print("\n[Bước 3: Tính Ma trận Chuyển vị (Hoán vị)]")

# Chuyển vị của A (kích thước n x m)
A_T = transpose_matrix(A, m, n)
print_matrix("Chuyển vị của A (A^T)", A_T)

# Chuyển vị của B (kích thước n x m)
B_T = transpose_matrix(B, m, n)
print_matrix("Chuyển vị của B (B^T)", B_T)

print("==================================================")