import math

# Nhập tọa độ điểm đi và điểm đến từ người dùng
x1, y1 = map(float, input("Nhập tọa độ điểm đi (x1, y1): "))
x2, y2 = map(float, input("Nhập tọa độ điểm đến (x2, y2): ").split(','))

# Tính độ dài quãng đường đi giữa hai điểm
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Tính số tiền cần trả
s = d * 8000

print("Số tiền cần trả là:", s)