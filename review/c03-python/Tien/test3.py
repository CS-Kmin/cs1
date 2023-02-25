# Tính số giờ và số phút ngủ
start_hour, start_minute, start_second = map(int, input("Nhập thời gian bắt đầu ngủ (giờ, phút, giây): ").split())
end_hour, end_minute, end_second = map(int, input("Nhập thời gian thức dậy (giờ, phút, giây): ").split())
if end_second >= start_second:
    delta_second = end_second - start_second
else:
    delta_second = end_second + 60 - start_second
    end_minute -= 1

if end_minute >= start_minute:
    delta_minute = end_minute - start_minute
else:
    delta_minute = end_minute + 60 - start_minute
    end_hour -= 1

delta_hour = end_hour - start_hour

# In kết quả
print("Thời gian ngủ là:", delta_hour, "giờ", delta_minute, "phút")