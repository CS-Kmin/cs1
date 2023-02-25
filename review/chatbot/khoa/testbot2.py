topic = ['lap trinh', 'tinh yeu', 'bong da', '1+1']
message = ['lap trinh cung ok nha', 'tinh yeu la loving thi phai', 'bong da hinh nhu la football ', 'bang 2']

unknow = ['xin loi, toi chua duoc huan luyen cau hoi nay!', 'xin loi, toi khong biet!']

test = ['lap trinh cung vui ma', 'cha biet tinh yeu la gi luon', 'thi la bong da soccer đó', 'theo toi la bang 2']

bot = 'Bot: '
print(bot + 'xin chao ban!')
user = input('You: ')

while user != 'bye':
    for i in range(0, len(topic)):
        # print(i)
        if user in topic[i] or topic[i] in user:
            print(bot + message[i])
            break
    else:
        print(bot + unknow[0])
        
    user = input('You: ')
    bot = 'Bot: '
    if user == 'bye':
        break
    #while user != 'bye':
    for k in range(0, len(topic)):
        if user in topic[k] or topic[k] in user:
            print(bot + test[k])
            break
    else:
        print(bot + unknow[1])

    user = input('You: ') 
    bot = 'Bot: '   

print(bot + 'cam on ban da su dung bot2.py!')