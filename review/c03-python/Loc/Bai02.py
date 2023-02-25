#Bài 2: Đặt xe
import math
NoiDi_X = input('Nhap toa do X noi di: ')
x1 = int(NoiDi_X)
NoiDi_Y = input('Nhap toa do Y noi di: ')
y1 = int(NoiDi_Y)
print("Toa do noi di: ",x1, y1)
NoiDen_X = input('Nhap toa do X noi den: ')
x2 = int(NoiDen_X)
NoiDen_Y = input('Nhap toa do Y noi den: ')
y2 = int(NoiDen_Y)
print("Toa do noi di: ",x2, y2)
#Công thức độ dài quãng đường
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
s = d * 8000
print("So tien nguoi dung can tra cho mot cuoc xe la: ", s)