# t06_mcp_tool - MCPサーバーとの統合

## 概要
MCPサーバー（ファイルシステム）と連携するエージェントの実装例です。ファイルシステムへのアクセスと操作方法を実装します。

cf. 公式ドキュメント: [MCP tools](https://google.github.io/adk-docs/tools/mcp-tools/)

## 学習内容
- `MCPToolset`を使用したMCP（Model Context Protocol）サーバーとの統合
- `StdioServerParameters`を使用したファイルシステムMCPサーバーの設定

## 実行方法

1. npxがインストールされていることなど、上記のサイトの前提条件を満たしていることを確認してください
1. 対象とするディレクトリを決めて、tools.pyの`TARGET_FOLDER_PATH`を設定してください。(デモではbooksを指定しています)

### Web UIで実行
```bash
cd tutorials
adk web
```
起動後にブラウザで`localhost:8080`を開き、ドロップダウンメニューより`t06_mcp_tool`を選択する

## 注意事項
- npxを使用してMCPサーバーを自動的に起動します
- ファイルシステムへのアクセスは`books/`ディレクトリに制限されています