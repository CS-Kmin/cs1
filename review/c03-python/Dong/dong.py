### Nên tách riêng mỗi bài trong 1 file nha
### Bài 3 có thể xử lý mọi trường hợp ko em? Làm thế nào có cách giải gọn hơn?

# #bt1

luongKi1 = input("Nhập lương kì 1: ")
luongKi2 = input("Nhập lương kì 2: ")

luongthuc = (int(luongKi1) + int(luongKi2)) - (int(luongKi1) + int(luongKi2))*0.05
print("Luong thực là : ",luongthuc)

# #bt2

print("Hãy nhập vào tọa độ điểm bắt đầu <>")
pointBegin_X = int(input("X: "))
pointBegin_Y = int(input("Y: "))
print("Hãy nhập vào tọa độ điểm kết thúc <>")
pointEnd_X = int(input("X: "))
pointEnd_Y = int(input("Y: "))
import math
distance = pow((pointBegin_X - pointEnd_X),2) + pow((pointEnd_X - pointEnd_Y),2)
distance = math.sqrt(distance)
money = distance*8000

print("Số tiền cần phải trả là: ",money)

## bt3

print("Nhập giờ đi ngủ: ")
sleep_h, sleep_m  , sleep_s = int(input("Giờ : ")),int(input("Phút: ")),int(input("Giây: "))
while sleep_h > 24 or sleep_m > 60 or sleep_s >60:
    print("Sai thông tỉn rồi , nhập lại đi nè :")
    sleep_h, sleep_m  , sleep_s = int(input("Giờ : ")),int(input("Phút: ")),int(input("Giây: "))

print("Nhập giờ thức dậy: ")
getup_h, getup_m  , getup_s = int(input("Giờ : ")),int(input("Phút: ")),int(input("Giây: "))
while getup_h > 24 or getup_m > 60 or getup_s >60:
    print("Sai thông tỉn rồi , nhập lại đi nè :")
    getup_h, getup_m  , getup_s = int(input("Giờ : ")),int(input("Phút: ")),int(input("Giây: "))

timetosleep_s = sleep_s + getup_s
timetosleep_m= sleep_m + getup_m
if sleep_h < getup_h:
    timetosleep_m = getup_h
else:
    timetosleep_h = (24 - sleep_h) + getup_h

if timetosleep_s >=60:
    timetosleep_m = int(timetosleep_s)/60 + timetosleep_m
    timetosleep_s = timetosleep_s % 60

if timetosleep_m >= 60:
    timetosleep_h = int(timetosleep_m/60) + timetosleep_h
    timetosleep_m = timetosleep_m % 60
import math
print(math.floor(timetosleep_h)," : ",timetosleep_m," : ",timetosleep_s)
##### bài nầy chỉ áp dụng cho trường hơp bạn ngủ vào tối hoặc khuya ngày hôm nay và thức dậy lúc sáng ngày hôm sau.





## bài 4S
n = int(input("Hãy nhập n: "))
for i in range(1,n+1):
    if i % 2 != 0:
        print(i," ")
        
## bài 5

Number1 = [1,2,-3,5,7,0,-2,-9]
for i in Number1:
    if i > 0:
        print(i," ")
        

# ## bài 6
Number2 = [1,2,-3,5,7,0,-2,-9]
for i in range(0,len(Number2)):
    if Number2[i] > 0:
        print(i," ")
        


