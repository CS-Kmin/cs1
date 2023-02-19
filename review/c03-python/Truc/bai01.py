luong_ky_1 = int(input("Nhập lương kỳ 1 của nhân viên: "))
luong_ky_2 = int(input("Nhập lương kỳ 2 của nhân viên: "))

tong_luong = luong_ky_1 + luong_ky_2
phi_bao_hiem = tong_luong * 0.05
luong_thuc_nhan = tong_luong - phi_bao_hiem

print("Lương thực nhận của nhân viên là:", luong_thuc_nhan)