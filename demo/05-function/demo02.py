# Viết hàm cho phép nhập vào 2 số và tính tổng 2 số đó.

# def tinhTong():
#     a=int(input("Moi nhap so a: "))
#     b=int(input("Moi nhap so b: "))
#     print("Tong = ", a+b)
# def main():
#     tinhTong()
# main()

###############

# c = None # Global

def tong(a, b):
    c = int(a) + int(b)
    return c # Trả về c ra ngoài lời gọi hàm

def main():
    k = tong(3, 6) * tong(2,3)
    print(k)

main()