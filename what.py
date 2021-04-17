import telegram
import pandas as pd
#token that can be generated talking with @BotFather on telegram
my_token = '1404973946:AAEIlBbWI-Wz7lwzCAW3IULhSFrpEsnfQC4'
bot = telegram.Bot(token=my_token)

def send(dep,sem,sub,f,l,i,token=my_token):
    """
    Send a mensage to a telegram user specified on chatId
    chat_id must be a number!
    """
    link = "<a href='http://127.0.0.1:5000/student?dep={}&sem={}&sub={}&id={}&f_name={}&l_name={}'>Click Here</a>".format(dep,sem,sub,i,f,l)
    bot.sendMessage(chat_id=i, text=link,parse_mode='HTML')
	
	
def call(dep,sem,sub):
    cl = pd.read_csv("./csv/{}.csv".format(dep+sem+sub))
    for f,l,i in zip(cl['F_name'],cl['L_name'],cl['chat_id']):
        
        send(dep,sem,sub,f,l,i)
    
