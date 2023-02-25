topic=["lap trinh","tinh yeu","bong da"]
messege1=["Lap trinh rat thu vi", "yeu la chet o trong long mot it", "Bong da rat huu ich cho moi nguoi"]
messege2=["Lap trinh phai hoc nhieu", "Tinh yeu la su hoa hop cua 2 nguoi", "Bong da la the thao vua"]
print('Chao mung ban den voi chatbot')
print('Ban nhap bye de thoat')
user=input("You: ")
bot="Bot: "
tp=""
bs1=""
bs2=""
y=1
yes=""
timthay=0
while user !="bye":
    for i in range(0,len(topic)): 
        if topic[i] in user:
            if y==1 :
                bot=bot+messege1[i]
                y=y+1
                timthay=1
            else:
                bot=bot+messege2[i]
                y=y-1 
                timthay=1
        ##i=i+1
    if timthay==0:
        print("Xin loi hien bot chua co thong tin")
        yes=input("Ban goi y giup 2 cau tra loi (y/n):")
        if yes=="y":
            tp=input("Nhap tu khoa: ")
            topic.append(tp)
            bs1=input("Nhap cau tra loi so 1: ")
            messege1.append(bs1)
            bs2=input("Nhap cau tra loi so 2: ")
            messege2.append(bs2)
            print("Cam on ban da cung cap thong tin")
            user=input("You: ")
            bot="Bot: "
        else:
            print("Cam on ban")
            user=input("You: ")
            bot="Bot: "   
    else:
        print(bot)
        user=input("You: ")
        bot="Bot: " 
        timthay = 0         
print("Xin hen gap lai")