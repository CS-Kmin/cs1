# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# In ra các số lẻ trong đoạn [1, n]
print("Các số lẻ trong đoạn [1, {}] là:".format(n))
for i in range(1, n+1):
    if i % 2 == 1:
        print(i)