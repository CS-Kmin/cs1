import random

topic = {'lap trinh':['lap trinh rat thu vi'],
         'tinh yeu':['yeu la chet trong long mot it'],
         'bong da':['bot la fan cua cr7']}

Greet = ['Xin chao', 'Hello', 'Chao ban']
Goodbyes = ['Tam biet ban', 'Hen gap lai lan sau', 'Bye bye!']

print('Bot:', random.choice(Greet))
user = input('You: ')
bot = 'Bot: '


while user != 'bye':
    for i in topic:
        if i in user:
            user_0 = user
            bot = bot + random.choice(topic[i])
            break
    else:
        print(bot + 'Bot khong biet dap an, xin moi ban cung cap dap an')
        ans = input('You: ')
        topic[user] = [ans]
        bot = bot + 'Bot cam on ban'

    print(bot)
    user = input('You: ')
    bot = 'Bot: '

    if user == 'cau tra loi khac':
        print(bot + 'Xin moi ban cung cap mot dap an khac')
        ans = input('You: ')
        topic[user_0].append(ans)
        print('Bot: Bot cam on ban')
        user = input('You: ')
    bot = 'Bot: '

if user == 'bye':
    print('Bot:', random.choice(Goodbyes))
