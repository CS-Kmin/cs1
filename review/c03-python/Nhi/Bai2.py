import math
xA = input("Nhập toạ độ x điểm hiện tại: ")
yA = input("Nhập toạ độ y điểm hiện tại: ")
xB = input("Nhập toạ độ x điểm cần đến: ")
yB = input("nhập toạ độ y điểm cần đến: ")
d = math.sqrt(pow((int(xB) - int(xA)), 2) + pow((int(yB) - int(yA)), 2))
s = d * 8000
print("Tiền người dùng cần trả là: ", s)
