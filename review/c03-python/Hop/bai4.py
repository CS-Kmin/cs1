# !!! range của em chưa chuẩn. Sẽ bị thiếu số 1 và số N nếu N là lẻ.

#bai4 : IN SO LE
N = int(input('Nhap vao mot so nguyen: '))
print('Cac so le trong doan tu 1 den',N)
for i in range(2,N):
    if i % 2 != 0:
        print(i)