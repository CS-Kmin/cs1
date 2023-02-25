hn=input('Nhap gio ngu: ')
mn=input('Nhap phut ngu :')
sn=input('Nhap giay ngu: ')
ht=input('Nhap gio thuc :')
mt=input('Nhap phut thuc :')
st=input('Nhap giay thuc: ')

if int(st)>int(sn): 
    ss=int(st)-int(sn)
else:
    ss=int(st)+60-int(sn)
    mt=int(mt)-1
if int(mt)>int(mn): 
    ms=int(mt)-int(mn)
else:
    ms=int(mt)+60-int(mn)
    ht=int(ht)-1
if int(ht)>int(hn):
    hs=int(ht)-int(hn)
else:
    hs=int(ht)+12-int(hn)
print('Thoi gian ngu: '+str(hs)+':'+str(ms)+':'+str(ss))