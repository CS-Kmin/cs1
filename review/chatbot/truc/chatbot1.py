import random

# Khai báo danh sách các lời chào và tạm biệt
greetings = ["Xin chào", "Chào bạn", "Hello", "Hi", "Hey"]
goodbyes = ["Tạm biệt", "Chào tạm biệt", "Hẹn gặp lại", "Bye"]

# Khai báo từ điển các chủ đề và câu trả lời tương ứng
topics = {
    "Thời tiết": ["Hôm nay trời nắng, nên bạn nên chuẩn bị áo mỏng nhé.", "Hôm nay có thể có mưa, bạn nên mang theo áo mưa.", "Hôm nay trời rất lạnh, nên bạn nên mặc quần áo ấm."],
    "Ẩm thực": ["Bạn nên thử đến nhà hàng ABC, họ có những món ăn ngon và giá cả phải chăng.","Tôi thấy nhà hàng XYZ rất được đông đảo khách hàng đánh giá cao về chất lượng ẩm thực.", "Nếu bạn thích ẩm thực địa phương, hãy đến quán LMN, nơi có những món ăn truyền thống tuyệt vời."]
}

# Hàm trả lời của chatbot
def chatbot_response(message):
    # Xử lý lời chào
    if message.lower() in ["hello", "hi", "hey", "xin chào", "chào bạn"]:
        return greetings[random.randint(0, len(greetings)-1)]
    
    # Xử lý lời tạm biệt
    if message.lower() in ["tạm biệt", "chào tạm biệt", "hẹn gặp lại", "bye"]:
        return goodbyes[random.randint(0, len(goodbyes)-1)]
    
    # Xử lý các chủ đề có trong từ điển
    for topic, responses in topics.items():
        if topic.lower() in message.lower():
            return responses[random.randint(0, len(responses)-1)]
    
    # Nếu không tìm thấy câu trả lời, yêu cầu người dùng cung cấp hướng dẫn
    response = input("Xin lỗi, tôi không biết về chủ đề này. Bạn có thể cho tôi biết câu trả lời được không? ")
    
    # Lưu câu trả lời của người dùng vào bộ nhớ và trả về câu trả lời cho người dùng
    topics[message] = [response]

    return response

# Hàm chạy chatbot
def run_chatbot():
    print("Chào mừng bạn đến với chatbot của tôi!")
    print("Hãy nói gì đó để bắt đầu hội thoại với tôi.")
    
    # Vòng lặp để chatbot lắng nghe và trả lời
    while True:
        message = input("Bạn: ")
        response = chatbot_response(message)
        print("Chatbot:", response)
        
        # Nếu người dùng nói "tạm biệt", chatbot sẽ kết thúc hội thoại
        if message.lower() in ["tạm biệt", "chào tạm biệt", "hẹn gặp lại", "bye"]:
            break

# Chạy chatbot
run_chatbot()
