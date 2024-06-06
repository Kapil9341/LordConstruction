import telepot


class TelegramBot:

    def __init__(self, chat_id, access_token):
        self.chat_id = chat_id
        self.bot = telepot.Bot(access_token)

    def sendMessage(self, message):
        try:
            self.bot.sendMessage(self.chat_id, message)
        except:
            pass

    # def sendDoc(self, docPath):
    #     self.bot.sendDocument(self.chat_id, document=open(docPath, 'rb'))
    #
    # def sendImage(self, imagePath):
    #     self.bot.sendPhoto(self.chat_id, photo=open(imagePath, 'rb'))


chat_id = '-1002078539468'  # for testing channel
access_token = '7027505705:AAHMl9A5G4JnbLQj6m9vG_SMoO_QOPIcS-g'  # for testing channel
# tb = TelegramBot(chat_id, access_token)

# tb.sendMessage("This is a test message from API")
# TelegramBot(chat_id, access_token).sendMessage('test lord')

# tb.sendDoc('Contact_us.xls')

# tb.sendDoc('E:\\photo.jpg')
