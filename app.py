from flask import Flask, request, abort

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

line_bot_api = LineBotApi('Iw7Vl/JkOmXPw27pnvbyqKUQQEaB/Byw0lUAPZ1V2yK+rANIW/gf1h+CAlq1hA0wiDlUW0FFy2jNEzIyFI6HRd5FsGWM9Q6rOqcYQ/kkTQo+ZRwB6kKfpdMmxVNaGTvC56OmOGwJAMn22dwWAFxEKgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e91d5308ed509ffe26a464423d0e8447')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    s = '你今天過得好嗎'
    msg = event.message.text
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text= s))


if __name__ == "__main__":
    app.run()