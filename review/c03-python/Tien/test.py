luong_ky_1 = int(input("Nhập lương kỳ 1: "))
luong_ky_2 = int(input("Nhập lương kỳ 2: "))

tong_luong = luong_ky_1 + luong_ky_2
phi_bhxh = 0.05 * tong_luong
luong_thuc_nhan = tong_luong - phi_bhxh

print("Lương thực nhận là:", luong_thuc_nhan)