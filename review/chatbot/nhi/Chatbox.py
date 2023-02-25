import random
topic = ["nganh", "hoc phi", "co so"]
message1 = ["co 30 nganh",  "Hoc phi hien nay khoang tu 13-24 trieu mot nam tuy nganh hoc", "co 2 co so nam o Thu Duc va Quan 1"]
message2 = ["Nhan van hien nay dang dao tao 30 nganh hoc", "dao dong tu 13-24 trieu mot nam", "Nhan van hien nay co 2 co so o Thu Duc va Quan 1"]
chao = ["Hello, ban co thac mac gi vay nhi?", "Chao ban, ban muon noi gi voi Bot nhỉ?", "Xin chao, ban muon hoi gi sao?"]
tamBiet = ["Byebye", "Tam biet", "Hen gap lai"]

bot = "Bot: "
value1 = random.choice(chao)
print(bot, value1)
user = input("You: ")

while user != "bye":
    for i in range(0, len(topic)):
        if topic[i] in user:
            x = random.randint(0, 1)
            if x == 0:
                bot = bot + message1[i]
            else:
                bot = bot + message2[i]
            print(bot)
            bot = "Bot: "
            break
        if i == len(topic) - 1:
            bot = bot + "Bot khong biet roi, ban co the noi cho Bot biet duoc khong?"
            print(bot)
            topic.append(user)
            user = input("You: ")
            message1.append(user)
            bot = "Bot: Ban con cach noi khac khong nhi?"
            print(bot)
            user = input("You: ")
            message2.append(user)
            bot = "Bot: Cam on ban. Ban con hoi gi nua khong?"
            print(bot)
            break
    user = input("You: ")
    bot = "Bot: "


value2 = random.choice(tamBiet)
print(bot, value2)
