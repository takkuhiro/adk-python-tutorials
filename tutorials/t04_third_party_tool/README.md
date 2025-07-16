# t04_third_party_tool - サードパーティツールの統合

## 概要
サードパーティが提供しているツールを利用するエージェントの実装例です。外部ツールとの連携方法を実装します。

cf. 公式ドキュメント: [Third party tools](https://google.github.io/adk-docs/tools/third-party-tools/)

## 学習内容
- `LangchainTool`を使用したLangChainツールの統合（Tavily検索）
- サードパーティツールをADKエージェントで使用する方法

## 実行方法

### 環境変数の設定
Tavily APIキーが必要です：
```bash
export TAVILY_API_KEY="your-api-key"
```

### Web UIで実行
```bash
# TODO: agent.pyのimport文を修正（from .tools import ...を使用）
cd tutorials
adk web
```
起動後にブラウザで`localhost:8080`を開き、ドロップダウンメニューより`t04_third_party_tool`を選択する

### ターミナルで実行
```bash
cd tutorials/t04_third_party_tool
python main.py
```