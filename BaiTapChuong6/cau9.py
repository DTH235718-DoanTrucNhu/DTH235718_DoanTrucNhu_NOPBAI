def is_prime(n):
    """Kiểm tra xem một số nguyên n có phải là số nguyên tố hay không."""
    if n < 2:
        return False
    # Chỉ cần kiểm tra từ 2 đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def process_array(M):
    """Phân loại và xuất các số lẻ, số chẵn, số nguyên tố từ list M."""
    
    # Khai báo các list để lưu trữ kết quả phân loại
    odd_numbers = []
    even_numbers = []
    prime_numbers = []
    non_prime_numbers = []

    # Duyệt qua từng phần tử trong list M
    for number in M:
        # Giả định đề bài muốn xử lý các số tự nhiên (nguyên dương)
        if not isinstance(number, int) or number < 1:
            continue # Bỏ qua nếu không phải số tự nhiên

        # Phân loại Chẵn/Lẻ
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
            
        # Phân loại Số nguyên tố / Không nguyên tố
        if is_prime(number):
            prime_numbers.append(number)
        else:
            non_prime_numbers.append(number)

    # Xuất kết quả ra màn hình
    print("==================================================")
    print("KẾT QUẢ XỬ LÝ MẢNG:")
    print("Mảng đầu vào (M):", M)
    print("--------------------------------------------------")
    
    # Dòng 1: Số lẻ
    print(f"Dòng 1: Gồm các số lẻ: {odd_numbers}")
    print(f"         Tổng cộng có: {len(odd_numbers)} số lẻ.")
    
    # Dòng 2: Số chẵn
    print(f"Dòng 2: Gồm các số chẵn: {even_numbers}")
    print(f"         Tổng cộng có: {len(even_numbers)} số chẵn.")

    # Dòng 3: Số nguyên tố
    print(f"Dòng 3: Gồm các số nguyên tố: {prime_numbers}")
    
    # Dòng 4: Số không phải là số nguyên tố
    print(f"Dòng 4: Gồm các số không phải là số nguyên tố: {non_prime_numbers}")
    print("==================================================")

# List đầu vào theo đề bài
M = [3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 5, 8]

# Thực thi chương trình
process_array(M)