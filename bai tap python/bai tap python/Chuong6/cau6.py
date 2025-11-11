import random

def generate_unique_random_list():
    """
    Hàm nhập N (số lượng phần tử) và tạo ra một list 
    chứa N số nguyên ngẫu nhiên, không trùng nhau.
    """
    
    # 1. Nhập N (số lượng phần tử mong muốn)
    while True:
        try:
            N = int(input("Nhập số lượng phần tử (N) cho list: "))
            if N <= 0:
                print("N phải là số nguyên dương.")
                continue
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

    # 2. Nhập phạm vi giá trị (từ min_val đến max_val)
    while True:
        try:
            min_val = int(input("Nhập giá trị tối thiểu (min_val): "))
            max_val = int(input("Nhập giá trị tối đa (max_val): "))
            
            if max_val < min_val:
                print("Lỗi: max_val phải lớn hơn hoặc bằng min_val.")
            elif (max_val - min_val + 1) < N:
                # Kiểm tra điều kiện để đảm bảo có thể tạo đủ N số không trùng nhau
                print(f"Lỗi: Phạm vi giá trị quá hẹp. Số lượng giá trị duy nhất khả dụng chỉ là {(max_val - min_val + 1)}. Vui lòng mở rộng phạm vi.")
            else:
                break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

    # 3. Tạo list chứa N số ngẫu nhiên KHÔNG TRÙNG NHAU
    # Phương pháp tốt nhất: Sử dụng random.sample() để chọn N phần tử duy nhất 
    # từ một tập hợp các số trong phạm vi (min_val đến max_val).
    
    # Tạo dãy số khả dụng
    available_numbers = range(min_val, max_val + 1)
    
    # Lấy ngẫu nhiên N số không trùng nhau
    random_list = random.sample(available_numbers, N)
    
    return random_list

# Thực thi hàm và in ra kết quả
final_list = generate_unique_random_list()
print("\n--- Kết quả ---")
print(f"List có {len(final_list)} số ngẫu nhiên KHÔNG TRÙNG NHAU là:")
print(final_list)