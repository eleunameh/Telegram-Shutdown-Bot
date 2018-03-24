import telegram
import os


def main():
    bot = telegram.Bot(token='bot token')  #Bot Token is needed to make the bot work

    global LAST_UPDATE_ID
    LAST_UPDATE_ID = bot.getUpdates()[-1].update_id  

    while True:
        for update in bot.getUpdates(offset=LAST_UPDATE_ID):
            text = update.message.text
            username=update.message.from_user.username
            chat_id = update.message.chat.id
            update_id = update.update_id
            if LAST_UPDATE_ID < update_id:
                if text=="shutdown" and username=="username":   #Checks if the message is sent by the right user and the content

                	try:
                       os.system('shutdown /s /t 5')
                        LAST_UPDATE_ID = update_id
                        bot.sendMessage(chat_id=update.message.chat_id, text="I shut down your computer, senpai! <3") #Sends a message that means the shut down has successfully happened.
                   	except:
                        	pass
                if text=="reboot" and username=="username":  #Checks if the message is sent by the right user and the content 
                        os.system('shutdown /r /t 5')
                        LAST_UPDATE_ID = update_id
                        bot.sendMessage(chat_id=update.message.chat_id, text="I rebooted your computer, senpai! <3") #Sends a message that means the reboot has successfully happened.
                if text=="Who is your daddy?" and username=="username": #Meme command just for the lulz, because I'm a weeb with a daddy kink Kappa.
				bot.sendMessage(chat_id=update.message.chat_id, text="Y-You... <3 *Blushes*")
				LAST_UPDATE_ID = update_id
				if username!="username": #If the username is not the one specified here, the bot sends this message and doesn't execute commands. This is made to prevent shutdowns by unauthorised people.
							bot.sendMessage(chat_id=update.message.chat_id, text="Sorry, but you're not my senpai, you can't talk to me >//<")
							LAST_UPDATE_ID = update_id
							
			
if __name__ == '__main__':
    main()
print encoded	
