import requests
import time

access_token = '***INSERT YOUR ACCESS TOKEN HERE***'

class TGBot(object):
	def __init__(self, access_token):
		self.access_token = access_token
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/getUpdates'		
		self.response = requests.get(self.ping_url).json()
		self.chat_id = self.response['result'][0]['message']['chat']['id']
		self.number_of_messages = len(self.response['result'])
		#return self.chat_id

	def send_message(self,message):
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/sendMessage?'+\
					'chat_id='+str(self.chat_id)+'&parse_mode=Markdown'+'&text='+message
		self.response = requests.get(self.ping_url)

	def send_photo(self,filepath):
		file_ = open(filepath,"rb")
		file_dict = {'photo':file_}
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/sendPhoto?'+\
					'chat_id='+str(self.chat_id)
		self.response = requests.post(self.ping_url,files=file_dict)
		file_.close()

	def check_new_message(self):
		self.ping_url = 'https://api.telegram.org/bot'+str(self.access_token)+'/getUpdates'
		self.response = requests.get(self.ping_url).json()
		if len(self.response['result']) > self.number_of_messages:
			new_message = self.response['result'][-1]['message']['text']
			self.number_of_messages = len(self.response['result'])
			print(new_message)

if __name__ == '__main__':
	bot = TGBot(access_token)
	#EXAMPLE ON SENDING MESSAGE
	bot.send_message('Hurray!!')
	#EXAMPLE ON SENDING PHOTO
	bot.send_photo('/mnt/d/bracelet2.JPG') 
	#CHECKING FOR NEW MESSAGES FROM USER
	stime = time.time()
	while time.time()-stime<100 :
		bot.check_new_message()

	#Appropriate file name for windows needs to be given
