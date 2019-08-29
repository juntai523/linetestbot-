from flask import Flask,request,abort
"""LINE Push"""
import json
import requests
from linebot import LineBotApi,WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent,TextMessage,TextSendMessage
import os
# HTTPヘッダを設定
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + '8Tv0bjRrDqSB7dktEL8fNQBD0k6HQx/bL2A+s1nf3jUSyWoqAgnB5F6gTZ7MMyahWxHm/ttUx3up/jrwPgJQnGynoDkJBvQ/R0172tOaDgOrzsHgjocj2gQ1MncovR3cgWj7a8YRmOXucbOOzNeaTAdB04t89/1O/w1cDnyilFU=',
}

# POSTデータを設定
POST = {
    "to": "Ua272a8de9e6a18856a679f997c474c80",
    "messages":[{
      "type": "flex",
      "altText": "This is a Flex Message",
      "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "25:35",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"}},
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [{
        "type": "text",
        "text": "ピーチプリンwithラズベリー",
        "weight": "bold",
        "size": "xl"}]},
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "商品詳細を見る",
          "uri": "https://www.starbucks.co.jp/food/dessert/4524785401327/?utm_content=official-rec&utm_medium=social&utm_source=LINE&utm_campaign=official"
        }
      },
      {
        "type": "spacer",
        "size": "sm"
      }
    ],
    "flex": 0
    }
   }
  }
 ]
}

POST2={"to": "Ua272a8de9e6a18856a679f997c474c80",
        "messages": [
        {"type": "template",
        "altText": "this is a buttons template",
        "template": {
            "type": "buttons",
            "text":  "スターバックスのおすすめカスタマイズから、あなた好みの一杯をみつけてみませんか？",
            "actions": [{
            "type": "message",
            "label": "カスタマイズをはじめる",
            "text": "カスタマイズをはじめる"}]}}]}

POST3 = {"to": "Ua272a8de9e6a18856a679f997c474c80",
         "messages": [
        {  
        "type": "flex",
        "altText": "this is a flex message",
        "contents": {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "今の気分で探す",
              "text": "今の気分で探す", }}]},
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "フレーバーで探す",
              "text": "フレーバーで探す", }}]},
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "メニューで探す",
              "text": "メニューで探す", }}]}]}}}]}

POST4 = {"to": "Ua272a8de9e6a18856a679f997c474c80",
         "messages": [
        {  
        "type": "flex",
        "altText": "this is a flex message",
        "contents": {
          "type": "bubble",
          "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "季節のおすすめ",
              "text": "季節のおすすめ", }}]},
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "休日のお出かけ",
              "text": "休日のお出かけ", }}]},
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "自分にご褒美",
              "text": "自分にご褒美", }}]},
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "集中したい",
              "text": "集中したい", }}]},
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "ゆっくりしたい",
              "text": "ゆっくりしたい", }}]},
                { "type": "box",
                "layout":"horizontal",
                "contents":[
                    {"type": "image",
              "url": "https://rs-j.adtdp.com/line-dev/10/carousel_image/pixta_29373431_M.jpg",
              "size": "xs",
              "flex":0},
            { "type": "button",
              "action":{
              "type": "message",
              "label": "リフレッシュに",
              "text": "リフレッシュに", }}]}]}}}]}

POST5 ={
  "to": "Ua272a8de9e6a18856a679f997c474c80",
  "messages": [
{
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
      "type": "carousel",
      "columns": [
          {
            "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
            "imageBackgroundColor": "#FFFFFF",
            "title": "キャラメル スモア フラペチーノ",
            "text": "サクサクの食感と濃厚なチョコレートフレーバーを楽しめる",
            "defaultAction": {
                "type": "message",
                "text": "How to orderを見る"
            },
            "actions": [
                {
                    "type": "message",
                    "label": "How to orderを見る",
                    "text": "How to orderを見る"
                },
            ]
          },
          {
            "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
            "imageBackgroundColor": "#000000",
            "title": "ピーチ オン ザ フラペチーノ",
            "text": "ピーチを存分に楽しめる",
            "defaultAction": {
                "type": "message",
                "text": "How to orderを見る"
            },
            "actions": [
                {
                    "type": "message",
                    "label": "How to orderを見る",
                    "text": "How to orderを見る"
                },
            ]
          },]}}]}
POST6 = {
    "to": "Ua272a8de9e6a18856a679f997c474c80",
    "messages":[{
      "type": "flex",
      "altText": "This is a Flex Message",
      "contents":{
  "type": "bubble",
  "hero": {
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "20:13",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
    },
    },
    "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [{
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "3:1",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
      }},{
    "type": "image",
    "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
    "size": "full",
    "aspectRatio": "3:1",
    "aspectMode": "cover",
    "action": {
      "type": "uri",
      "uri": "http://linecorp.com/"
      }},
    ]},
    }}]}
app=Flask(__name__)
#環境変数の取得
YOUR_CHANNEL_ACCESS_TOKEN="8Tv0bjRrDqSB7dktEL8fNQBD0k6HQx/bL2A+s1nf3jUSyWoqAgnB5F6gTZ7MMyahWxHm/ttUx3up/jrwPgJQnGynoDkJBvQ/R0172tOaDgOrzsHgjocj2gQ1MncovR3cgWj7a8YRmOXucbOOzNeaTAdB04t89/1O/w1cDnyilFU="
YOUR_CHANNEL_SECRET="b5297119b48490ae322185b38605c56b"
line_bot_api=LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler=WebhookHandler(YOUR_CHANNEL_SECRET)

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
        if event.message.text == "\u4eca\u9031\u306e\u304a\u3059\u3059\u3081":
            #今週のおすすめ
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='こちらが今週のおすすめです。'))
            # 実行
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST))
            print(REQ.status_code)
            # HTTPステータスが 200 だったら OK
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u30ab\u30b9\u30bf\u30de\u30a4\u30ba\u3092\u306f\u3058\u3081\u308b":
            #カスタマイズ
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST3))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u30ab\u30b9\u30bf\u30de\u30a4\u30ba":
            #カスタマイズをはじめる
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST2))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u4eca\u306e\u6c17\u5206\u3067\u63a2\u3059":
            #今の気分で探す
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST4))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "\u5b63\u7bc0\u306e\u304a\u3059\u3059\u3081":
            #季節のおすすめ
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST5))
            print(REQ.status_code)
            if REQ.status_code != 200:
                print(REQ.text)
        elif event.message.text == "How to order\u3092\u898b\u308b":
            #how to order
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='How to order'))
        elif event.message.text == "\u30d4\u30c3\u30af\u30a2\u30c3\u30d7":
            #ピックアップ
            REQ = requests.post(CH, headers=HEADERS, data=json.dumps(POST6))
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
 
