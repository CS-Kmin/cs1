import math
xdi = int(input('nhap x di: '))
ydi = int(input('nhap y di: '))
xden = int(input('nhap x den: '))
yden = int(input('nhap y den: '))
d = math.sqrt((xdi - xden)**2 + (ydi-yden)**2)
s = d * 8000
print(s)
