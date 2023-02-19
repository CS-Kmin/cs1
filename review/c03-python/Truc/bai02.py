import math

# Nhập tọa độ nơi đi và nơi đến
x1, y1 = map(float, input("Nhập tọa độ nơi đi (x1, y1): ").split(","))
x2, y2 = map(float, input("Nhập tọa độ nơi đến (x2, y2): ").split(","))

# Tính khoảng cách giữa 2 điểm trên bản đồ
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Tính tiền cước
fare = distance * 8000

# In kết quả
print("Khoảng cách giữa nơi đi và nơi đến là: {:.2f}".format(distance))
print("Số tiền cần trả cho cuốc xe là: {:.2f} VNĐ".format(fare))