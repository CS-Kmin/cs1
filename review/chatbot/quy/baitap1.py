user = input("you:")
bot = "bot:"
topic = ["xin chao", "tam biet"]
message = ["xin chao hom nay ban the nao", "tam biet chuc ban mot ngay vui ve"]
for i in  range(0, len(topic)):
     if user in topic [i]:
        print(bot + message[i])