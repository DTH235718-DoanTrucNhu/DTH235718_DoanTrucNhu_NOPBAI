def input_sorted_list():
    """
    Hàm nhập vào một dãy số theo thứ tự tăng dần, 
    yêu cầu nhập lại nếu nhập sai quy tắc.
    """
    
    # List để lưu trữ các số đã nhập
    sorted_numbers = []
    
    # Số cuối cùng đã được nhập thành công (dùng để kiểm tra quy tắc tăng dần)
    last_number = None 
    
    print("--- CHƯƠNG TRÌNH NHẬP DÃY SỐ TĂNG DẦN ---")
    print("Nhập 'done' hoặc 'ketthuc' bất cứ lúc nào để dừng.")

    while True:
        user_input = input(f"Nhập số tiếp theo (lớn hơn {last_number if last_number is not None else 'số đầu tiên'}): ")
        
        # 1. Kiểm tra điều kiện dừng
        if user_input.lower() in ['done', 'ketthuc']:
            break
            
        # 2. Kiểm tra và chuyển đổi sang số
        try:
            current_number = float(user_input) # Dùng float để chấp nhận cả số nguyên và số thực
        except ValueError:
            print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập một SỐ hoặc 'done' để kết thúc.")
            continue
            
        # 3. Kiểm tra quy tắc tăng dần
        if last_number is not None and current_number <= last_number:
            print(f"Lỗi quy tắc: Số {current_number} KHÔNG LỚN HƠN số đã nhập trước đó ({last_number}). Vui lòng nhập lại.")
            continue
            
        # 4. Nhập thành công: Cập nhật list và số cuối cùng
        sorted_numbers.append(current_number)
        last_number = current_number
        print(f"Đã thêm. Dãy số hiện tại: {sorted_numbers}")

    # 5. In kết quả cuối cùng
    print("\n==================================")
    print("Dãy số đã nhập sau khi hoàn thành:")
    
    if sorted_numbers:
        # Nếu list không rỗng
        # Chuyển đổi các số float sang int nếu chúng là số nguyên để hiển thị đẹp hơn
        display_list = [int(n) if n == int(n) else n for n in sorted_numbers]
        print(display_list)
    else:
        print("Không có số nào được nhập.")
    print("==================================")

# Thực thi hàm
input_sorted_list()