# !!! Testcase này bị sai nè
# Nhập thời gian bắt đầu ngủ (hh:mm:ss): 5:10:20
# Nhập thời gian thức dậy (hh:mm:ss): 3:10:10
# Thời gian ngủ là: 22 giờ -1 phút

# Nhập thời gian bắt đầu ngủ và thời gian thức dậy
start_time = input("Nhập thời gian bắt đầu ngủ (hh:mm:ss): ")
end_time = input("Nhập thời gian thức dậy (hh:mm:ss): ")

# Tách giờ, phút, giây từ chuỗi thời gian
start_hour, start_minute, start_second = map(int, start_time.split(":"))
end_hour, end_minute, end_second = map(int, end_time.split(":"))

# Tính thời gian ngủ
if end_hour >= start_hour:
    total_hour = end_hour - start_hour
else:
    total_hour = 24 - start_hour + end_hour

if end_minute >= start_minute:
    total_minute = end_minute - start_minute
else:
    total_hour -= 1
    total_minute = 60 - start_minute + end_minute

if end_second >= start_second:
    total_second = end_second - start_second
else:
    total_minute -= 1
    total_second = 60 - start_second + end_second

# In kết quả
print("Thời gian ngủ là: {} giờ {} phút".format(total_hour, total_minute))