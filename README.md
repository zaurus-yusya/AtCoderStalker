# AtcoderStalker

## サービス概要

AtCoder上でライバルが問題を解いたら、そのことをあなたのLINEに通知してくれるサービスです。

以下のQRコードをLINEで読み込むことで登録できます。

LINEのチャットボットでの対話でどのユーザーが問題を解いた時に通知をもらうか登録できます。
以後ストーキングリストへの登録と呼びます。

LINEへの通知は1日2回(9:00と20:00)に送られます。

AtCoderのレートを上げたいユーザーにおいて、勉強のために問題を解くことのモチベーションアップとなるサービスを目指して作りました。
周りが勉強している様子を観測し、良い意味で危機感と緊張感を芽生えさせることができると嬉しいです。

## アピールポイント

自らがAtCoderを意識していない時でも受動的に情報を得ることができるサービスとすることを目的としました。

push通知を送る仕組み、またユーザーのアカウント登録の障壁をなるべく軽減するために、多くの方がインストールしている可能性の高いLINEを活用しました。

大きく分けて以下の2つのロジックから成ります。

- LINEのチャットボットを通じたストーキングリストへの登録
- ストーキングリストの登録内容・登録されたAtCoderのユーザーの問題を解いた状況を集計してLINEユーザーにpush通知を送信

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
EnvMap:　以下の環境変数を設定

```
sam build
sam deploy --guided
```