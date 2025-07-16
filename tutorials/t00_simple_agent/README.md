# t00_simple_agent - シンプルな天気エージェント

## 概要
最もシンプルなエージェントの実装例です。都市名を入力すると、その都市の天気を回答するシンプルな機能を持つエージェントを実装します。

cf. 公式ドキュメント: [Quickstart](https://google.github.io/adk-docs/get-started/quickstart/)

## 学習内容
- `Agent`クラスの基本的な使い方（name, model, description, instruction パラメータ）
- エージェントへの`tools`パラメータによる関数の登録方法

## 実行方法

### Web UIで実行
```bash
cd tutorials
adk web
```

起動後にブラウザで`localhost:8080`を開き、ドロップダウンメニューより`t00_simple_agent`を選択する
