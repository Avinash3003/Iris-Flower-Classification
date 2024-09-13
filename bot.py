import telebot
import ast
import pickle
import requests


model=pickle.load(open('SVM.pickle','rb'))

botToken='5973735720:AAG0vG7D_0g_fJFbeFwbOWktAYz7Xo9o7X0'
bot=telebot.TeleBot(
    botToken,
    parse_mode=None)

# handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Welcome to my Bot\n\n1.Enter sepal length in cm\n 2. sepal width in cm\n3. petal length in cm\n4. petal width in cm\n\nInput format Comma(,) separated\nEg:-12,23,20,17")

@bot.message_handler(regexp="[a-zA-Z0-9_🎈😊⭐💕📰😂❤️😍🤣😒]")
def handle_message(message):
    # print(message)
    message=str(message)
    
    k=ast.literal_eval(message)
    userid=k['from_user']['id']
    try:
        #yoe=float(k['text'])
        #print(yoe)
        a=k['text'].split(",")
        b=type(k['text'])
        print(b)
        for i in range(len(a)):
            a[i]=float(a[i])
            
        result=model.predict([a])[0]
        if str(result)=="iris_setosa":
            img=open('setosa.jpg','rb')
        elif str(result)=="iris_versicolor":
            img=open('versi.jpg','rb')
        else:
            img=open('virginica.jpg','rb')
        m=a
        if(max(m)>25):
            bot.send_message(int(userid),'Enter input range(<25)')
        else:
            bot.send_photo(int(userid),img)
            bot.send_message(int(userid),'Flower predicted according to the inputs is "'+str(result)+"\"")
    except:
        print('Invalid\nEnter 4 valid int/float inputs')
        bot.send_message(int(userid),'Invalid input\nEnter 4 valid int/float inputs')

bot.polling()