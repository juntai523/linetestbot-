from flask import Flask,request,abort
import json
import requests
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage
import os
from os.path import join, dirname
from dotenv import load_dotenv

app=Flask(__name__)
load_dotenv(join(dirname(__file__),".env"))
#環境変数の取得
token=os.environ.get("YOUR_CHANNEL_ACCESS_TOKEN")
secret=os.environ.get("YOUR_CHANNEL_SECRET")
line_bot_api=LineBotApi(token)
handler=WebhookHandler(secret)

# HTTPヘッダを設定
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token,
}

app=Flask(__name__)
load_dotenv(join(dirname(__file__),".env"))

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
    f = open("post.json","r")
    json_data=json.load(f)
    profile = line_bot_api.get_profile(event.source.user_id)
    if event.message.type == "text":
        CH = 'https://api.line.me/v2/bot/message/push'
        if event.message.text == "\u4eca\u9031\u306e\u304a\u3059\u3059\u3081":
            #今週のおすすめ
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='こちらが今週のおすすめです。'))
            # 実行
            json_data["Recommended_thisweek"]["to"]=profile.user_id
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["Recommended_thisweek"]))
            print(REQ.status_code)
            # HTTPステータスが 200 だったら OK
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u30ab\u30b9\u30bf\u30de\u30a4\u30ba":
            #カスタマイズ
            json_data["customize"]["to"]=profile.user_id
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["customize"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u30ab\u30b9\u30bf\u30de\u30a4\u30ba\u3092\u306f\u3058\u3081\u308b":
            #カスタマイズをはじめる
            json_data["start_customize"]["to"]=profile.user_id
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["start_customize"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u4eca\u306e\u6c17\u5206\u3067\u63a2\u3059":
            #今の気分で探す
            json_data["Feeling_now"]["to"]=profile.user_id
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["Feeling_now"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u5b63\u7bc0\u306e\u304a\u3059\u3059\u3081":
            #季節のおすすめ
            json_data["Seasonal_recommendations"]["to"]=profile.user_id
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["Seasonal_recommendations"]))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "How to order\u3092\u898b\u308b":
            #how to order
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='How to order'))
        elif event.message.text == "\u30d4\u30c3\u30af\u30a2\u30c3\u30d7":
            #ピックアップ
            json_data["pick_up"]["to"]=profile.user_id
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(json_data["pick_up"]))
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

 
