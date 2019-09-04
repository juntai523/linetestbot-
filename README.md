# linetestbot-
スタバのラインボットの動作を模倣したbot

◯コードの概略

main.py

送られてきた文字に対応してPOSTメッセージを送信。それ以外に関しては所定のメッセージを送信。

post.json

POSTするデータをjsonファイルにて管理。
各jsonデータの"to"="~"にはYour user IDを記載。

◯リッチメニューの作成

LINE official Account Manager にてラインアカウントに紐づくbotのリッチメニューを作成。

手順　
1.LINE official Account Managerのホームでリッチメニューを作成

２.タイトル:リッチメニューのタイトルを入力（任意）

３.ステータス:オンにチェック

4.表示期間：表示したい期間を設定

5.メニューバーのテキスト：その他のテキストにチェック、（ほっとするブレイクタイム）と入力。＊（）の文字がラインのメニューバーに反映される

6.メニューのデフォルト表示：表示するにチェック

7.コンテンツ設定

（１）テンプレートを選択：分割の方法とリッチメニューのサイズを選択。＊テンプレートに無い形式を利用するには、リッチメニューのjsonデータを作る必要あり

（２）背景画像をアップロード：画面右のデザインガイドを選択→テンプレートガイドをダウンロード→背景画像をアップロードでテンプレートが画像をアップロード。（今回はmediumの４分割）

8.アクションを設定
(1)選択した範囲をタップした際のアクションを設定（今回はAからDの４つ）。タイプにてテキストを選択しテキストを入力（A：今週のおすすめ、B：カスタマイズ、C：ピックアップ）。
タイプにてリンクを選択(D:スターバックス公式のURLを設定。テキストを入力（任意））。

９.保存
