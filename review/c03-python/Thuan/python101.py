# Bài 1: Ứng dụng kế toán

luongKy01 = input('Nhập lương kỳ 1: ')
luongKy02 = input('Nhập lương kỳ 2: ')
baohiem = 0.05
luongThucLanh = int(luongKy01) + int(luongKy02) # !!! Biến luongThucLanh nên lưu giá trị lương thực lãnh (áp công thức vào đây lun nha)

print('Lương thực lãnh: ', luongThucLanh - int(luongThucLanh*baohiem))

# Bài 2: Đặt xe
### Bài này bị sai input nha
d = input("Nhập độ dài quãng đường: ")
s = int(d) * 8000
print('Số tiền cần phải trả cho quãng đường: ', s)

# Bài 3: Misfit shine
### Em có thể tự code bài này mà không dùng hàm có sẵn được không?
import datetime

start_time = datetime.datetime.strptime(input('Nhập giờ bắt đầu ngủ với định dạng HHMMSS: '), '%H%M%S')
end_time = datetime.datetime.strptime(input('Nhập giờ tỉnh với định dạng HHMMSS: '), '%H%M%S')

sleep_time = end_time - start_time
print(sleep_time)

# Bài 4: In số lẻ
### Bài này sẽ sai nếu n là số lẻ
n = int(input('Nhập số nguyên: '))
for i in range(1,n):
    if i % 2 != 0:
        print(i)

# Bài 4: In số lẻ
a = [-99, 50, -60, 39, 100, 7, 0]
for i in a:
    if i > 0:
        print(i)

# Bài 6: In chỉ số của số âm
a = [-99, 50, -60, 39, 100, 7, 0]
for i in range(len(a)):
    if a[i] > 0:
        print(i)