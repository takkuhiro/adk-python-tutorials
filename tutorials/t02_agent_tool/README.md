# t02_agent_tool - Tool Callingの実装

## 概要
Tool Callingの実装方法を学ぶためのサンプルです。Google検索ツールと短編小説を書くツールを実装し、エージェントがツールを呼び出して機能を拡張する方法を学びます。

cf. 公式ドキュメント: [Function Tools](https://google.github.io/adk-docs/tools/function-tools/)

## 学習内容
- `AgentTool`を使ったエージェントのツール化（エージェントを別のエージェントのツールとして使用）
- `LongRunningFunctionTool`を使った長時間実行関数のツール化

## 実行方法

### Web UIで実行
```bash
# TODO: agent.pyのimport文を修正（from .tools import ...を使用）
cd tutorials
adk web
```
起動後にブラウザで`localhost:8080`を開き、ドロップダウンメニューより`t02_agent_tool`を選択する

### ターミナルで実行
```bash
# .envファイルを設定
cp .env.template .env
# .envを編集して必要な値を設定
source .env

# agent.pyのimport文を修正（from tools import ...を使用）
cd tutorials/t02_agent_tool
python main.py
```

## 注意事項
- 実行方法によってimport文を切り替える必要があります（agent.py内のコメント参照）