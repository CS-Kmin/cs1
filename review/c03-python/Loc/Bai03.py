#Bài 3: Misfit shine
print("Thoi gian bat dau ngu")
start_hour, start_minute, start_second = 11, 30, 0
print('Gio:',start_hour , 'Phut:',start_minute, 'Giay:',start_second)
print("Thoi gian thuc day")
end_hour, end_minute, end_second = 18, 20, 0
print('Gio:',end_hour , 'Phut:',end_minute, 'Giay:',end_second)
# Tính khoảng thời gian giữa thời điểm bắt đầu ngủ và thời điểm thức dậy
if end_hour < start_hour:
    end_hour += 24

hour_diff = end_hour - start_hour
minute_diff = end_minute - start_minute
second_diff = end_second - start_second

if second_diff < 0:
    second_diff += 60
    minute_diff -= 1

if minute_diff < 0:
    minute_diff += 60
    hour_diff -= 1

# Chuyển khoảng thời gian sang đơn vị giờ và phút
total_minutes = hour_diff * 60 + minute_diff
hours = total_minutes // 60
minutes = total_minutes % 60

# In ra thời gian ngủ
print("Thời gian ngủ là:", hours, "giờ", minutes, "phút")