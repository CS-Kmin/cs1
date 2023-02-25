topics = ["lap trinh", "tinh yeu", "bong da"]
messages = ["Bạn cần hỏi gì về lập trình?", "Bạn cần hỏi gì về tình yêu?", "Bạn cần hỏi gì về bóng đá?", "Tôi không hiểu câu hỏi của bạn."]

message1 = [
    "DINH NGHIA:Lập trình là việc sử dụng ngôn ngữ lập trình để tạo ra phần mềm máy tính, trò chơi, trang web, ứng dụng.",
    "PHUONG PHAP HOC:Để học lập trình tốt, bạn cần phải chăm chỉ và siêng năng.",
    "DIA DIEM HOC:Bạn có thể học lập trình ở các trường đại học như FPT, RMIT, HUTECH hoặc các trung tâm nổi tiếng như Kmin.",
    "VI TRI UNG TUYEN:Lập trình có nhiều mảng như backend, frontend, data analytics,..."
]

message2 = [
    "DINH NGHIA:Tình yêu là sự kết hợp giữa bản năng và lý trí giữa giới tính nam và giới tính nữ.",
    "CAM XUC:Tình yêu có thể mang lại hạnh phúc nhưng cũng có thể gây đau khổ.",
    "TO TINH:Bạn có thể mua một bông hoa và tỏ tình với người mình thích."
]

message3 = [
    "Messi và Ronaldo là hai cầu thủ xuất sắc nhất hiện nay.",
    "Giải bóng đá lớn nhất thế giới là World Cup.",
    "Tôi rất yêu bóng đá <3."
]

print("Bot: Chào bạn, hãy nhập vào câu hỏi của bạn hoặc nhập 'bye' để thoát.")

while True:
    user_input = input("You: ").lower()
    if user_input == "bye":
        print("Bot: Tạm biệt!")
        break
    found_topic = False
    for i in range(len(topics)):
        if topics[i] in user_input:
            found_topic = True
            if i == 0:
                print("Bot: " + messages[i])
                input_user2 = input("You: ").lower()
                for j in range(len(message1)):
                    if input_user2 in message1[j].lower():
                        print("Bot: " + message1[j])
                        break
                else:
                    print("Bot: Tôi không hiểu câu hỏi của bạn.")
            elif i == 1:
                print("Bot: " + messages[i])
                input_user2 = input("You: ").lower()
                for j in range(len(message2)):
                    if input_user2 in message2[j].lower():
                        print("Bot: " + message2[j])
                        break
                else:
                    print("Bot: Tôi không hiểu câu hỏi của bạn.")
            elif i == 2:
                print("Bot: " + messages[i])
                input_user2 = input("You: ").lower()
                for j in range(len(message3)):
                    if input_user2 in message3[j].lower():
                        print("Bot: " + message3[j])
                        break
                else:
                    print("Bot: Tôi không hiểu câu hỏi của bạn.")
            elif i == 3 and "bóng đá" in user_input:
                print("Bot: Bạn muốn tìm hiểu gì về bóng đá?")
                input_user2 = input("You: ").lower()
                if "messi" in input_user2:
                    print("Bot: " + message3[0])
                elif "ronaldo" in input_user2:
                    print("Bot: " + message3[0])
                elif "world cup" in input_user2:
                    print("Bot: " + message3[1])
                elif "yêu bóng đá" in input_user2:
                    print("Bot: " + message3[2])
                else:
                    print("Bot: Tôi không hiểu câu hỏi của bạn.")
            else:
                print("Bot: Tôi không hiểu câu hỏi của bạn.")
            break
    if not found_topic:
        print("Bot: Tôi không hiểu câu hỏi của bạn.")


