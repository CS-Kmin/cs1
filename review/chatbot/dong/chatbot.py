import random
#### Tạo ra 2 list xin chào và tạm biệt sau đó tạo thêm 2 biến random để random từ vị tri
### thứ 0 đến len - 1 để random câu chào và tạm biệt
say_Hello = ["Xin chào!!", "Chào bạn chúc bạn một ngày tốt lành !!!", "Xin chào. Bạn có thể hỏi tôi bất cú thứ gì nè!!"]
say_Goodbye = ["Bye bye. Cảm ơn vì đã trò chuyện với tôi.", "Tạm biệt  bạn chúc bạn một ngày tốt lành !!!", "Cảm ơn tôi rất vui khi nói chuyện với bạn."]



sayHello_RD = random.randint(0,len(say_Hello)-1)### biến random cho list sayhelloo
say_Goodbye_RD = random.randint(0,len(say_Goodbye)-1)
botMsg= "Bot: "
print(botMsg,say_Hello[sayHello_RD])
user=input("You:  ")



topics = ["tinh yeu","bong da", "lap trinh"] ## tạo list các chủ đề
msg = ["Được ai đó yêu sâu sắc mang lại cho bạn sức mạnh; yêu một người sâu sắc mang lại cho bạn dũng khí.",##tưf 0 đén 3 laf các câu chủ đề của topics[0]
       "Cuộc sống không có tình yêu giống như cây không có hoa, trái.",
       "Một mình chúng ta có thể làm rất ít; cùng nhau chúng ta có thể làm rất nhiều trong tình yêu.",
       "Không có sự quyến rũ nào bằng sự dịu dàng của trái tim.",
       "Bóng đá rất tuyệt vời",## từ 4 đến 7 là các  câu trả lơif của chủ đề topics[1]
       "Bóng đá không chỉ chơi bằng đôi chân, hãy chơi bằng cả trái tim của bạn",
       "Bóng đá giống như cuộc sống, chúng ta cần mục tiêu",
       "Tài năng chơi bóng đá chỉ có 5%, còn lại đó là sự luyện tập chăm chỉ, đánh vỡ cực hạn của bản thân.",
       "Những devloper nổi tiếng đều gặp phải những vấn đề nan giải cho đến khi họ giải quyết được nó",## từ 8 đến 11 là các  câu trả lơif của chủ đề topics[2]
       "Một trong những kĩ năng lập trình tuyệt nhất mà bạn có thể học được là biết khi nào mình nên bỏ đi một thời gian",
       "Nhờ có lập trình thì tôi mới có thể trò chuyện được với bạn",
       "Chưa có ai có thể viết được một phần mềm hoàn hảo, bạn cũng vậy"]




while user != "bye":
    flag = False ## tạo biến cờ 
    index_RD_start= 0 
    index_RD_end = 3
    botMsg= "Bot: "
    for i in range(0,len(topics)):
        index_Msg = random.randint(index_RD_start,index_RD_end) ### random vị trí câu trả lời theo tường chue đề 
        if topics[i] in user:## nếu chủ đề thứ i là con của user (câu hỏi người dùng vừa nhập) gán biến botMsg cho botMsg cộng với list msg tại vị trí vừa random
            botMsg = botMsg + msg[index_Msg]
            flag = True ## biến flag trả về giá trị true khi điều kiện trên đúng
        index_RD_start = index_RD_start + 4 ## tăng vị trí random lên 4 dơn vị để random câu trả lời phù hoưpj với câu hỏi
        index_RD_end = index_RD_end + 4
    if flag:   
        print(botMsg)## nếu như flag trê trả về giá trị bằng true thì in biến botMgs vuằ được gán 
    else:
        botMsg= "Bot: "# 
        topics.append(user)# thêm chủ đề người dùng vừa nhập vào list cuối list topics
        print(botMsg,"Tôi không thể trả lời được câu hỏi của bạn.")
        print(botMsg,"Xin hãy hướng dẫn tôi đẻ sử dụng nó")    
        user_add=input("You:  ")##  người dùng nhập câu trả lời cho câu vừa hỏi
        print("Bot: Tôi đã hiểu rồi. Cảm ơn bạn rất nhiều")
        len_msg = (len(msg)+ 3)
        for j in range(len(msg)-1,len_msg):## gán câu trả lời vào cuối Msg
            msg.append(user_add)
    user=input("You:  ")
say_Goodbye_RD = random.randint(0,len(say_Goodbye)-1)
botMsg= "Bot: "
if user == "bye":
    print(botMsg,say_Goodbye[say_Goodbye_RD])