sinhVien = ['Khoa', 'Tien', 'Quy', 'Hien']
s = input('Nhap ten: ')

# for value in sinhVien:
#     if s in value:
#         print(value)

for index in range(0, len(sinhVien)):
   if s in sinhVien[index]:
        print(index)

# if s in sinhVien[1]:
#     print('yes')
