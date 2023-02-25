#Bài 4: In số lẻ
songuyen = input('Nhap vao so nguyen n: ')
n = int(songuyen)
i = 1
print("Cac so le la: ")
for i in range(n+1):
    if i % 2 != 0:
        print(i)