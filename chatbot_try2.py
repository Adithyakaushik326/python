from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
bot = ChatBot('bot')
trainer=ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
while True:
	msg=input('you:')
	if msg != 'bye':
		res=bot.get_response(msg)
		print('chatbot:' ,res)
	if msg == 'bye':
		print('chatbot: bye!')
		break
			