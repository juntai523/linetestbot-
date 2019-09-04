from flask import Flask,request,abort
import json
import requests
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage
import os

#環境変数の取得
YOUR_CHANNEL_ACCESS_TOKEN="8Tv0bjRrDqSB7dktEL8fNQBD0k6HQx/bL2A+s1nf3jUSyWoqAgnB5F6gTZ7MMyahWxHm/ttUx3up/jrwPgJQnGynoDkJBvQ/R0172tOaDgOrzsHgjocj2gQ1MncovR3cgWj7a8YRmOXucbOOzNeaTAdB04t89/1O/w1cDnyilFU="#ラインボットのアクセストークン
YOUR_CHANNEL_SECRET="b5297119b48490ae322185b38605c56b"#ラインボットのChannel Secret
line_bot_api=LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler=WebhookHandler(YOUR_CHANNEL_SECRET)

# HTTPヘッダを設定
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + YOUR_CHANNEL_ACCESS_TOKEN,
}

app=Flask(__name__)
@app.route("/callback",methods=["POST"])
def callback():
    signature=request.headers["X-Line-Signature"]

    body=request.get_data(as_text=True)
    app.logger.info("Request body"+body)

    try:
        handler.handle(body,signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

@handler.add(MessageEvent)
def handle_message(event):
    if event.message.type == "text":
        #print(event)
        CH = 'https://api.line.me/v2/bot/message/push'
        f = open("post.json","r")
        json_data=json.load(f)
        #print(json_data)
        if event.message.text == "\u4eca\u9031\u306e\u304a\u3059\u3059\u3081":
            #今週のおすすめ
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='こちらが今週のおすすめです。'))
            # 実行
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["POST1"]))
            print(REQ.status_code)
            # HTTPステータスが 200 だったら OK
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u30ab\u30b9\u30bf\u30de\u30a4\u30ba":
            #カスタマイズをはじめる
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["POST2"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u30ab\u30b9\u30bf\u30de\u30a4\u30ba\u3092\u306f\u3058\u3081\u308b":
            #カスタマイズ
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["POST3"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u4eca\u306e\u6c17\u5206\u3067\u63a2\u3059":
            #今の気分で探す
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["POST4"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u5b63\u7bc0\u306e\u304a\u3059\u3059\u3081":
            #季節のおすすめ
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["POST5"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "How to order\u3092\u898b\u308b":
            #how to order
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='How to order'))
        elif event.message.text == "\u30d4\u30c3\u30af\u30a2\u30c3\u30d7":
            #ピックアップ
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["POST6"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        else:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='メッセージありがあとうございます。こちらのアカウントから返信はできません。スターバックスでほっとする幸せなブレイクタイムをお過ごしください。'))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='メッセージありがあとうございます。こちらのアカウントから返信はできません。スターバックスでほっとする幸せなブレイクタイムをお過ごしください。'))

if __name__=="__main__":
    port=int(os.getenv("PORT",5000))
    app.run(host="0.0.0.0",port=port)

 
