from flask import Flask, request, abort
import os
import re
import timer
import message
import serial_arduino

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/")
def hello_world():
  return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']

  # get request body as text
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  # handle webhook body
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)

  return 'OK'


def post_later(times, userid):
  timer.timer(*times)
  line_bot_api.push_message(userid, TextSendMessage(text='時間が来たニャ！'))
  serial_arduino.send_serial()


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  received_message = event.message.text
  userid = event.source.user_id
  print("userid: {}".format(userid))
  print("message: {}".format(received_message))
  reply_message,times = message.create_reply_and_times(received_message)
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=reply_message))
  if times:
    post_later(times, userid)

if __name__ == "__main__":
#    app.run()
  port = int(os.getenv("PORT"))
  app.run(host="0.0.0.0", port=port)
