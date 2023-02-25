import random
Chao = ["CHAO MUNG BAN DEN VOI CHATBOT AI", "WELCOME TO CHATBOT AI", "GRATAM CHATBOT AI"]
Tam_biet = ["TAM BIET. HEN GAP LAI!!!", "GOODBYE. SEE YOU AGAIN!!!", "VALE. TE VIDERE ITERUM!!!"]
val_Chao = random.randint(0, 2)
if val_Chao in range(0, len(Chao)):
    print(Chao[val_Chao])
Cau_hoi = input('Nhap cau hoi nguoi dung muon hoi: ')
bot = "Bot: "
topic = ["lap trinh", "kinh te", "bong da", "dien anh"]
mes = ["ngon ngu lap trinh duoc tim kiem nhieu nhat la python.", "kinh te Viet Nam dang tang truong nhanh.", "nha vo dich C1 hien tai la Real Madric", "Jame Cameron la mot nha lam phim, dao dien noi tieng the gioi."]
Python = "Python là một ngôn ngữ lập trình bậc cao cho các mục đích lập trình đa năng, do Guido van Rossum tạo ra và lần đầu ra mắt vào năm 1991.Python được thiết kế với ưu điểm mạnh là dễ đọc, dễ học và dễ nhớ. Python là ngôn ngữ có hình thức rất sáng sủa, cấu trúc rõ ràng, thuận tiện cho người mới học lập trình và là ngôn ngữ lập trình dễ học; được dùng rộng rãi trong phát triển trí tuệ nhân tạo."
Kinhte = "Kinh tế là tổng hòa các mối quan hệ tương tác lẫn nhau của con người và xã hội - liên qua trực tiếp đến việc sản xuất, trao đổi, phân phối, tiêu dùng các loại sản phẩm hàng hóa và dịch vụ nhằm thỏa mãn nhu cầu ngày càng cao của con người trong một xã hội với một nguồn lực có giới hạn. Kinh tế dùng để chỉ phương pháp sản xuất bao gồm cả lực lượng sản xuất và quan hệ sản xuất, chỉ tổng hợp quan hệ vật chất trong xã hội phù hợp với trình độ phát triển của lực lượng sản xuất."
Bongda = "Bóng đá được xem là môn thể thao thu hút nhất trên thế giới, có đến hàng vạn người đến sân vận động để xem các trận đá bóng, và hàng triệu người ngồi ở nhà theo dõi qua màn hình tivi. Với luật chơi đơn giản, ít tốn kém, đề cao tinh thần đồng đội, bóng đá ở nhiều quốc gia có sức ảnh hưởng vô cùng to lớn trong cuộc sống của người hâm mộ, trong cộng đồng địa phương hay cả quốc gia; do đó có thể nói đây là môn thể thao phổ biến nhất thế giới."
Dienanh = "Jame Cameron la la mot nha lam phim, dao dien noi tieng the gioi. Ong la cha de cua nhieu bo phim dien anh noi tieng Hollywood nhu: “The Terminator” (1984), “Aliens” (1986), “Alita: Battle Angel” (2019), ...Dac biet, ong la dao dien duy nhat so huu hai bo phim dat danh thu hon 3 ty do la: “Titanic” (1997) va “Avatar” (2009)"
mes_update = (Python, Kinhte, Bongda, Dienanh)
while Cau_hoi != 'bye':
    for index in range(0, len(topic)):
        if topic[index] in Cau_hoi:
            what = input("Ban muon biet kien thuc co ban hay chuyen sau: ")
            bot1 = "Bot: "
            if what == "chuyen sau":
                print(mes_update[index])
                break
            else:
                print(mes[index])
                break
    if topic[index] not in Cau_hoi:
        print("Toi khong biet dieu nay. Ban co the huong dan them giup toi khong!!!")
        Hoc = input("Bot: ")
        print("Vay: ", Hoc, ".Cam on ban da giup.")
        topic.append(Cau_hoi)
        mes.append(Hoc)
    Cau_hoi = input('Nhap cau hoi nguoi dung muon hoi: ')
    bot = "Bot: "
    if Cau_hoi == 'bye':
        val_Tam_biet = random.randint(0, 2)
        if val_Tam_biet in range(0, len(Tam_biet)):
            print(Tam_biet[val_Tam_biet])
            break