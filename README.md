# AtcoderStalker

## サービス概要

AtCoder上でライバルが問題を解いたら、そのことをあなたのLINEに通知してくれるサービスです。

<img src="https://user-images.githubusercontent.com/54097621/125200226-0d90b280-e2a5-11eb-929d-62e71ac8f6ab.png" width=400px>

サービスURL:  https://line.me/R/ti/p/@381fkvdg

以下のQRコードをLINEで読み込むことでも登録できます。

<img src="https://user-images.githubusercontent.com/54097621/125200274-5183b780-e2a5-11eb-92d5-9643ceae3ca9.png" width=150px>

LINEのチャットボットでの対話でどのユーザーが問題を解いた時に通知をもらうか登録できます。

※以後ストーキングリストへの登録と呼びます。

LINEへの通知は1日2回(9:00と20:00)に送られます。

<img src="https://user-images.githubusercontent.com/54097621/125200331-8728a080-e2a5-11eb-8a93-918fa4f370e0.jpg" width=400px>

AtCoderのレートを上げたいユーザーにおいて、勉強のために問題を解くことのモチベーションアップとなるサービスを目指して作りました。
周りが勉強している様子を観測し、良い意味で危機感と緊張感を芽生えさせることができると嬉しいです。

※詳しい記事　
https://note.com/zaurus/n/n3ca56c3305c7

## ポイント

ユーザーが受動的に情報を得ることができるサービスとすることで、ユーザーがAtCoderに取り組んでいないタイミングでも勉強の意識を芽生えさせることを目的としました。

push通知を送る仕組み、またユーザーのアカウント登録の障壁をなるべく軽減するために、多くの方がインストールしている可能性の高いLINEを活用しました。

大きく分けて以下の2つのロジックから成ります。

- LINEのチャットボットを通じたストーキングリストへの登録
- ストーキングリストの登録内容・AtCoderのユーザーの問題を解いた状況を集計してLINEユーザーにpush通知を送信

## 使用技術

言語・ライブラリ等
- python 3.8.6
- LINE Messaging API
  - line-bot-sdk-python 

    https://github.com/line/line-bot-sdk-python
- AWS
  - Lambda
  - API Gateway
  - DynamoDB
  - CloudWatch
  - IAM

アプリケーション構築
- AWS SAM 1.19.1

## システム構成

<img src="https://user-images.githubusercontent.com/54097621/125200884-c3f59700-e2a7-11eb-98f1-b95a9f8824d8.png" width=800px>

①Lambda：LINEのチャットボットを通じたストーキングリストへの登録

②Lambda：ストーキングリストの登録内容・AtCoderのユーザーの問題を解いた状況を集計してLINEユーザーにpush通知を送信

## 機能
- LINE bot
  - LINEの友達追加/削除時のユーザー管理
  - ストーキングリストへの登録/削除
  - 現在登録しているストーキングリストの確認
- 定期実行
  - ストーキングリストへ登録されたAtCoderユーザーの問題を解いた状況の確認・集計
  - 全LINEユーザーのストーキングリストへの登録状況集計
  - LINEユーザーへのpush通知送信

## Getting Started

AWS CLI バージョン2のインストール
```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```

AWSアカウント情報の設定
```
aws configure
```

AWS SAM CLI のインストール
```
brew install aws-sam-cli
```

## Deploy

template_b.yamlをtemlate.yamlにrename

yamlファイルのEnvMap:　以下の環境変数を設定

その後下記コマンド実行
```
sam build
sam deploy --guided
```
