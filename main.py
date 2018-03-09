from microsoftbotframework import MsBot
from tasks import *
from flask import Flask
app = Flask(__name__)

bot=MsBot()
bot.add_process(echo_response)

@app.route('/test')
def hello_world():
  return 'Hello, World!'

if __name__=='__main__':
    bot.run()
    app.run()
