### Tạo danh sách tương tự bài 5

n = int(input('Nhap n: '))
arr = [-n, n+1]
for i in range(0, len(arr)):
    if i in arr[i]:
        print(i)