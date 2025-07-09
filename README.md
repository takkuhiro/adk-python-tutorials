# ADK Python チュートリアル

このリポジトリは、Google製のAgent Development Kit (ADK)のPythonバージョンのチュートリアル集です。ADKを使用してインテリジェントなエージェントを開発する方法を段階的に学ぶことができます。

## 概要

ADK（Agent Development Kit）は、Googleが開発したオープンソースのエージェント開発フレームワークです。このフレームワークを使用することで、タスク指向の自律的なAIエージェントを効率的に開発することができます。

## チュートリアル構成

このリポジトリには以下の5つのチュートリアルが含まれています：

0. **Weather Agent** (`samples/tutorial0_weather_agent/`)
   - 基本的なエージェントの作成方法を学びます
   - 天気情報を取得・解析するシンプルなエージェントの実装例

1. **Multi Agents** (`samples/tutorial1_multi_agents/`)
   - 複数のエージェントを連携させる方法を学びます
   - メインエージェントと分析・要約を行うサブエージェントの連携例

2. **Agent Tool** (`samples/tutorial2_agent_tool/`)
   - エージェントにツールを実装する方法を学びます
   - カスタムツールの作成と統合方法の解説

3. **Code Executor** (`samples/tutorial3_code_executor/`)
   - エージェントにコード実行機能を追加する方法を学びます
   - プログラムの動的実行とその結果の処理方法

4. **Third Party Tool** (`samples/tutorial4_third_party_tool/`)
   - サードパーティツールの統合方法を学びます
   - 外部ツールやAPIとの連携例

## 環境設定

### 必要条件
- Python 3.8以上
- pip または uv（パッケージマネージャー）

### インストール方法

1. リポジトリのクローン:
```bash
git clone [repository-url]
cd adk-python-tutorials
```

2. 依存パッケージのインストール:
```bash
uv pip install -e .
```

## 対応していない範囲
- Apigeeを用いたツール: https://google.github.io/adk-docs/tools/google-cloud-tools/#apigee-api-hub-tools
- Application Integrationを用いたツール: https://google.github.io/adk-docs/tools/google-cloud-tools/#application-integration-tools


## 使用方法

各チュートリアルディレクトリには個別のREADMEファイルが用意されています。チュートリアルを順番に進めることで、ADKの機能を段階的に学ぶことができます。

## 参考リンク

- [Agent Development Kit 公式ドキュメント](https://google.github.io/adk-docs/)
