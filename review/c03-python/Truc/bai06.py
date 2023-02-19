# Cho trước danh sách các số nguyên
numbers = [-1, 2, 0, -3, 5, 7, -4, 6]

# In ra các chỉ số của các số âm trong danh sách
print("Các chỉ số của các số âm trong danh sách là:")
for i in range(len(numbers)):
    if numbers[i] < 0:
        print(i)