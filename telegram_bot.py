import requests

access_token = '***INSER YOUR ACCESS TOKEN HERE***'

class TGBot(object):
	def __init__(self, access_token):
		self.access_token = access_token
		self.chat_id = ''

	def get_chat_id(self):
		ping_url = 'https://api.telegram.org/bot'+access_token+'/getUpdates'		
		response = requests.get(ping_url).json()
		self.chat_id = response['result'][0]['message']['chat']['id']
		#return self.chat_id

	def send_message(self,message):
		ping_url = 'https://api.telegram.org/bot'+access_token+'/sendMessage?'+\
					'chat_id='+str(self.chat_id)+'&parse_mode=Markdown'+'&text='+message
		response = requests.get(ping_url)

	def send_photo(self,filepath):
		file = open(filepath,"rb")
		file_dict = {'photo':file}
		ping_url = 'https://api.telegram.org/bot'+access_token+'/sendPhoto?'+\
					'chat_id='+str(self.chat_id)
		response = requests.post(ping_url,files=file_dict)
		file.close()

if __name__ == '__main__':
	bot = TGBot(access_token)
	bot.get_chat_id()
	bot.send_message('***ENTER YOUR MESSAGE HERE***')
	bot.send_photo('***ENTER FILE PATH HERE***') 
