#a
def tong_uoc(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s
def la_so_hoan_thien(n):
    return tong_uoc(n) == n
#b
def la_so_thinh_vuong(n):
    return tong_uoc(n) > n
for num in [6, 12, 28, 20, 15]:
    print(num, ":")
    print("  Hoàn thiện?", la_so_hoan_thien(num))
    print("  Thịnh vượng?", la_so_thinh_vuong(num))

