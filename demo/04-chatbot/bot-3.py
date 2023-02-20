topic = ["lap trinh", "tinh yeu", "bong da"]
message = ["lap trinh rat thu vi", "yeu la chet o trong long mot it", "bot la fan cua m10 va cr7"]

user = input("You: ")
bot = "Bot: "

while user != "bye":
    for i in range(0, len(topic)):
        if topic[i] in user:
            bot = bot + message[i]
    print(bot)
    user = input("You: ")
    bot = "Bot: "
