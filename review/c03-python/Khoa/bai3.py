gioN, phutN, giayN = int(input('Nhap gioN: ')), int(input('Nhap phutN: ')), int(input('Nhap giayN: '))
gioT, phutT, giayT = int(input('Nhap gioT: ')), int(input('Nhap phutT: ')), int(input('Nhap giayT: '))

if 0 <= gioN <= gioT <= 23 and 0 <= phutN and phutT <=59 :
        if phutN == phutT :
                print( 'Thoi gian ngu la: ',(gioT - gioN),'gio,', (phutT - phutN), ' phut')
        if 0 <= phutN < phutT <= 59 :
                print( 'Thoi gian ngu la: ',(gioT - gioN),'gio,', (phutT - phutN), ' phut')
        if 59 >= phutN > phutT >= 0 :
                print( 'Thoi gian ngu la: ',(gioT - gioN - 1),'gio,', (phutT + (60 - phutN)), ' phut')
elif 0 <= gioT <= gioN <= 23 and 0 <= phutN and phutT <=59 :
        if phutN == phutT :
                print( 'Thoi gian ngu la: ',((24 - gioN) + gioT),'gio,', (phutN - phutT), ' phut')
        if 0 <= phutN < phutT <= 59 :
                print( 'Thoi gian ngu la: ',((24 - gioN) + gioT),'gio,', (phutT - phutN), ' phut')
        if 59 >= phutN > phutT >= 0 :
                print( 'Thoi gian ngu la: ',((24 - gioN) + gioT - 1),'gio,', (phutT + (60 - phutN)), ' phut')