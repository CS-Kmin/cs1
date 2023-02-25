gioBatDau = int(input('nhap gio bat dau: '))
phutBatDau = int(input('nhap phut bat dau: '))
giayBatDau = int(input('nhap giay bat dau: '))
gioThucGiay = int(input('nhap gio thuc day: '))
phutThucGiay = int(input('nhap phut thuc day: '))
giayThucGiay = int(input('nhap giay thuc day: '))

tongSoGiayBatDau = gioBatDau * 3600 + phutBatDau * 60 + giayBatDau
tongSoGiayThucDay = gioThucGiay * 3600 + phutThucGiay * 60 + giayThucGiay

### Có thể tính ra số âm không em?
tongSoGiayNgu = tongSoGiayThucDay - tongSoGiayBatDau 
# print(tongSoGiayNgu)

TongGioNgu = int(tongSoGiayNgu / 3600)
print(TongGioNgu, 'gio')

TongSoGiayConDu = tongSoGiayNgu % 3600

TongSoPhutNgu = int(TongSoGiayConDu / 60)
print(TongSoPhutNgu, 'phut')
