print('Hi bạn, rất rất vui được gặp bạn nè.')
user = input('You: ')
bot = 'Bot: '
topic = ['lập trình','tình yêu', 'bóng đá', 'thầy cô']
message = ['Tớ đang học hỏi thêm về lập trình nè', 'Tình yêu là những ánh sáng lấp lánh đèn vàng thắp lên bên ô cửa nhỏ', 'Bóng đá yêu nhất là Việt Nam rồi', 'Mái trường mến yêu đó bạn']
while 'bye' not in user:
    a = '0'
    for x in range(0, len(topic)):
        if topic[x] in user:
            a = bot + message[x]
            print(a)
    b = a[5:len(a)]
    if b not in message:
        print(bot + 'Xin lỗi bạn, tôi không biết, bạn có thể hướng dẫn tôi không?')
    user = input('You: ') 
print(bot + 'Bye nhé, gặp lại bạn sau.')