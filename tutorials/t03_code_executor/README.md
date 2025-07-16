# t03_code_executor - コード実行機能

## 概要
コード実行機能を持つエージェントの実装例です。エージェントがプログラムコードを実行する方法を実装します。

cf. 公式ドキュメント: [Built-in Tools](https://google.github.io/adk-docs/tools/built-in-tools/)

## 学習内容
- `BuiltInCodeExecutor`を使用したコード実行機能の実装
- `code_executor`パラメータによるエージェントへのコード実行機能の追加

## 実行方法

### Web UIで実行
```bash
# TODO: agent.pyのimport文を修正（from .tools import ...を使用）
cd tutorials
adk web
```
起動後にブラウザで`localhost:8080`を開き、ドロップダウンメニューより`t03_code_executor`を選択する

### ターミナルで実行
```bash
cd tutorials/t03_code_executor
python main.py
```