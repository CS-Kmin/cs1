a, b = int(input('Nhap a: ')), int(input('Nhap b: '))
e, f = int(input('Nhap e: ')), int(input('Nhap f: '))

import math
d = int(math.sqrt(((e-a) ** 2) + ((f-b) ** 2)))

s = int(d*8000)

print('So tien can tra la: ',s)