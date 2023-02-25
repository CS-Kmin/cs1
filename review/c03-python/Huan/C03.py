import math
conf=1
while 1:
    print("C03 - Luyện tập lập trình Python")
    print("1. Ứng dụng kế toán")
    print("2. Đặt xe")
    print("3. Misfit shine")
    print("4. In số lẻ")
    print("5. In số dương")
    print("6. In chỉ số của số dương")
    print("0. Thoát")
    conf=int(input("Noi nhap: "))
    if conf==1:
       x=int(input("Mời nhập lương kỳ 1: "))
       x=x+int(input("Mời nhập lương kỳ 2: ")) ### Nên tách 2 biến, sẽ làm chương trình dễ hiểu hơn
       print("Lương thực nhận của nhân viên: ")
       print(0.95*x)
    if conf==2:
       x1=int(input("Mời nhập tọa độ x của điểm đi: "))
       y1=int(input("Mời nhập tọa độ y của điểm đi: "))
       x2=int(input("Mời nhập tọa độ x của điểm đến: "))
       y2=int(input("Mời nhập tọa độ y của điểm đến: "))
       d=math.sqrt((x2-x1)**2 + (y2-y1)**2)
       s=d*8000
       print("Số tiền cần trả: ", s)
    if conf==3:
        gio1=int(input("Mời nhập giờ ngủ: "))
        phut1=int(input("Mời nhập phút ngủ: "))
        giay1=int(input("Mời nhập giây ngủ: "))
        gio2=int(input("Mời nhập giờ dậy: "))
        phut2=int(input("Mời nhập phút ngủ: "))
        giay2=int(input("Mời nhập giây ngủ: "))
        if giay2>=giay1:
            giay=giay2-giay1
        else :
           giay=60-(giay1-giay2)
        if phut2>=phut1:
            phut=phut2-phut1
        else :
           phut=60-(phut1-phut2) ### Nếu chương trình nhảy vào else ở if số 1 (xét giây), thì công thức này liệu có đúng?
        if gio2>=gio1 and phut2>=phut1:
            gio=gio2-gio1
        else:
           gio=gio2-gio1-1
        print("Số giờ ngủ: ", gio, phut ,giay)
    if conf==4:
       n=int(input("Mời nhập số nguyên n: "))
       for i in range(1,n+1):
          if i%2==1:
             print(i, " ")
    if conf==5:
       arr=[ 1, 2, 3, 4, 5, -1, -3, -9, -12]
       for i in range(0, len(arr)):
          if int(arr[i])>0:
             print(arr[i], " ")
    if conf==6:
       arr=[ 1, 2, 3, 4, 5, -1, -3, -9, -12]
       for i in range(0, len(arr)):
          if int(arr[i])>0:
             print("Các chỉ số dương: ", i, " ")
    if conf == 0:
      break
print("Xin cam on")


  

