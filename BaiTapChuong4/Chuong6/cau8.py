def input_and_sort_descending():
    """
    Hàm nhập vào một dãy N số thực, sau đó sắp xếp dãy số theo thứ tự giảm dần
    và xuất ra kết quả.
    """
    
    # 1. Nhập số lượng phần tử (N)
    while True:
        try:
            n = int(input("Nhập số lượng phần tử (N) trong dãy số: "))
            if n > 0:
                break
            else:
                print("N phải là một số nguyên dương.")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")

    # 2. Nhập N số thực vào list M
    M = []
    print(f"\nVui lòng nhập {n} số thực (có thể là số nguyên hoặc số thập phân):")
    
    for i in range(n):
        while True:
            try:
                # Nhập số M[i]
                number = float(input(f"Nhập phần tử M[{i}]: "))
                M.append(number)
                break
            except ValueError:
                print("Đầu vào không hợp lệ. Vui lòng nhập một số thực.")

    # 3. Sắp xếp dãy số theo thứ tự GIẢM DẦN
    # Sử dụng phương thức .sort() với tham số reverse=True
    M.sort(reverse=True) 
    
    # 4. Xuất ra dãy số sau khi sắp xếp
    print("\n--- KẾT QUẢ ---")
    print("Dãy số ban đầu đã được sắp xếp theo thứ tự GIẢM DẦN là:")
    
    # Hiển thị đẹp hơn: Chuyển đổi các số float sang int nếu chúng là số nguyên
    display_list = [int(num) if num == int(num) else num for num in M]
    print(display_list)
    print("---------------")

# Thực thi hàm
input_and_sort_descending()