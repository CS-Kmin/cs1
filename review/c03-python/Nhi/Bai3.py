gioNgu = 11
phutNgu = 10
giayNgu = 40
gioDay = 5
phutDay = 15
giayDay = 10
if gioNgu > 12:
    gioNgu = gioNgu - 12
if gioDay > 12:
    gioDay = gioDay - 12
if giayDay >= giayNgu:
    giay = giayDay - giayNgu
    if phutDay >= phutNgu:
        phut = phutDay - phutNgu
        if gioDay >= gioNgu:
            gio = gioDay - gioNgu
        else:
            gio = (12 - gioNgu) + gioDay
    else:
        phut = (phutDay + 60) - phutNgu
        gioDay = gioDay - 1
        if gioDay >= gioNgu:
            gio = gioDay - gioNgu
        else:
            gio = (12 - gioNgu) + gioDay
else:
    giay = (giayDay + 60) - giayNgu
    phutDay = phutDay - 1
    if phutDay >= phutNgu:
        phut = phutDay - phutNgu
        if gioDay >= gioNgu:
            gio = gioDay - gioNgu
        else:
            gio = (12 - gioNgu) + gioDay
    else:
        phut = (phutDay + 60) - phutNgu
        gioDay = gioDay - 1
        if gioDay >= gioNgu:
            gio = gioDay - gioNgu
        else:
            gio = (12 - gioNgu) + gioDay
print("Thời gian ngủ là: ", gio, "tiếng", phut, "phút")