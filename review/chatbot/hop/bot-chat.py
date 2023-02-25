topic = ["chung khoan","python","Kmin","cong nghe thong tin"]
message = ["chung khoan la mot bang chung tai san hoac phan von cua cong ty hay to chuc da phat hanh",
           "Python la mot ngon ngu lap trinh bac cao, de hoc va de hieu",
           "Kmin la trung tam day Cong Nghe Thong Tin",
           "Lam lap trinh vien, chuyen vien phan tich du lieu, kiem duyet chat luong phan mem, ..v..v"
           ]
bot  = "Bot: "
print(bot,"Xin chao !! Ban dang tham gia chat cung Bot")
user = input("You: ")
while user != "bye":
    for i in range(0,len(topic)):
        if topic[i] in user:
            bot = bot + message[i]
    if bot != "Bot :":
        print(bot)   
    else:
        print("Xin loi, thong tin khong nam trong hieu biet cua Bot!")  
    user = input("You: ")
    bot  = "Bot :"
print(bot,"Ban da thoat cuoc hoi dap cung Bot")