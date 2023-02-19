# !!! Bài này đúng rồi, nhưng đoạn if-else là không cần thiết nha. Em suy ngẫm thử.

print("Nhap diem di (x,y):")
x = input('x: ')
y = input('y: ')
print("Nhap diem den (x,y): ")
a = input('x: ')
b = input('y: ')
if int(x) - int(a) > 0:
    c = int(x) - int(a)
else:
    c = - int(x) + int(a)
if int(y) - int(b) > 0:
    d = int(y) - int(b)
else:
    d = - int(y) + int(b)
import math
s = math.sqrt(c*c+d*d)*8000
print(s)
