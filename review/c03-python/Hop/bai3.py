# !!! Không nên làm thay đổi data của input nha em.
# Lưu ý: Người ngủ có thể ngủ bất kỳ giờ nào. -> Em thiếu trường hợp này

#bai3 Misfit shine 
a = [8,10,10]
b = [10,25,25]
print('sleep start time (hh:mm:ss):',a[0],":",a[1],":",a[2])
print('make up time (hh:mm:ss)    :',b[0],":",b[1],":",b[2])
#quy dinh thoi gian ngu tu 18 - > sau 24 gio toi 
if a[0] in range(18,24):
    if b[1] >= a[1]:
        a[0] = (24 - a[0]) +  b[0]
        a[1] = b[1] - a[1]
    else:
        a[0] = (24 - a[0]) +  b[0] - 1 
        a[1] = (60 - a[1]) + b[1]
#quy dinh thoi gian ngu tu 0 - > sau 6h sang
elif a[0] in range(0,6):
    if b[1] >= a[1]:
        a[0] = b[0] - a[0]
        a[1] = b[1] - a[1]
    else:
        a[0] = b[0] - a[0] - 1 
        a[1] = (60 - a[1]) + b[1]
print('time to sleep (hh:mm)      :',a[0],':',a[1])
