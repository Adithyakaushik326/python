from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
bot=ChatBot('Bot')
trainer = ListTrainer(bot)
# for files in os.listdir('D:/Projects/python practice/chatbot/chatterbot-corpus/chatterbot_corpus/data/english/'):
# 	data=open('D:/Projects/python practice/chatbot/chatterbot-corpus/chatterbot_corpus/data/english/' + files ,'r').readlines()
# 	trainer.train(data)
while True:
	msg=input('you:')
	if msg != 'bye':
		res=bot.get_response(msg)
		print('chatbot:' ,res)
	if msg == 'bye':
		print('chatbot: bye!')
		break
			