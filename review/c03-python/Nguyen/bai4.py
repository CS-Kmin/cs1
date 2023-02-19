### Kết quả sẽ ra sai nếu a là một số lẻ.
a = input('Nhap so: ')
for x in range(0, int(a)):
    if x % 2 == 1:
        print(x)