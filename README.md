# ADK Python 実践チュートリアル

このリポジトリは、Google製のAgent Development Kit (ADK)のPythonバージョンのチュートリアル集です。

ADKを使用してインテリジェントなエージェントを開発する方法を段階的に学ぶことができます。

## ADKとは

ADK（Agent Development Kit）は、Googleが開発したオープンソースのエージェント開発フレームワークです。

このフレームワークを使用することで、タスク指向の自律的なAIエージェントを効率的に開発することができます。

## よくある間違い集

よくある間違いやアンチパターン、ADKのバグなどは [PROBLEMS.md](/PROBLEMS.md) に記載しています

実装上詰まったことがあれば、まずはこちらのドキュメントをご確認ください


## チュートリアル構成

このリポジトリには以下のチュートリアルが含まれています：

1. **Simple Agent** (`tutorials/t00_simple_agent`)
   - 最もシンプルなエージェントの実装例です。
   - 都市名を入力すると、その都市の天気を回答するシンプルな機能を持つエージェントを実装します。

2. **Multi Agents** (`tutorials/t01_multi_agents`)
   - 複数のエージェントを組み合わせたシステムの実装例です。
   - メインエージェントの下に要約エージェントと目標分析エージェントを配置し、さらに目標分析エージェントの下に褒めるエージェントと厳しいアドバイスをくれるエージェントを配置した階層構造を実装します。

3. **Agent Tool** (`tutorials/t02_agent_tool`)
   - Tool Callingの実装方法を学ぶためのサンプルです。
   - Google検索ツールと短編小説を書くツールを実装し、エージェントがツールを呼び出して機能を拡張する方法を学びます。

4. **Code Executor** (`tutorials/t03_code_executor`)
   - コード実行機能を持つエージェントの実装例です。
   - エージェントがプログラムコードを実行する方法を実装します。

5. **Third Party Tool** (`tutorials/t04_third_party_tool`)
   - サードパーティが提供しているツールを利用するエージェントの実装例です。
   - 外部ツールとの連携方法を実装します。

6. **Cloud SQL Tool** (`tutorials/t05_cloud_sql_tool`)
   - Google CloudのCloud SQLと連携するエージェントの実装例です。
   - Toolboxを使用してCloud SQLに接続し、データベース操作を行う方法を実装します。

7. **MCP Tool** (`tutorials/t06_mcp_tool`)
   - MCPサーバー（ファイルシステム）と連携するエージェントの実装例です。
   - ファイルシステムへのアクセスと操作方法を実装します。

8. **State** (`tutorials/t07_state`)
   - ADKのSession & Memory機能の使用方法を学ぶためのチュートリアルです。
   - エージェントの状態管理、セッション管理、メモリ機能の活用方法を実装します。

9. **Deploy** (`tutorials/t08_deploy`)
   - ADKで作成したエージェントのデプロイ方法を学ぶためのチュートリアルです。
   - Agent Engine、Cloud Run、GKEへのデプロイ方法を実装します。

10. **Execution** (`tutorials/t09_execution`)
    - エージェントの実行方法の違いを学ぶためのチュートリアルです。
    - Web UI、Runner、AdkAppなど、異なる実行方法の特徴と使い分けを実装します。

11. **Callback** (`tutorials/t10_callback`)
    - ADKのCallback機能の使用方法を学ぶためのチュートリアルです。
    - エージェントの実行前後での処理の追加、入出力の編集、ガードレールの実装方法を学びます。

12. **Evaluate** (`tutorials/t11_evaluate`)
    - ADKの評価機能を学ぶためのチュートリアルです。
    - Tool Callingの正確性評価やレスポンスの一致度評価（ROUGE）の方法を実装します。

13. **Artifacts** (`tutorials/t12_artifacts`)
    - ADKのArtifacts機能の使用方法を学ぶためのチュートリアルです。
    - バイナリデータ（画像、ファイル、音声など）の管理とLLMでの利用方法を実装します。

## 環境設定

### 必要条件
- Python 3.8以上
- pip または uv（パッケージマネージャー）

### インストールから実行まで

1. リポジトリのクローン:
```bash
git clone [repository-url]
cd adk-python-tutorials
```

2. 依存パッケージのインストール:
```bash
uv pip install -e .
```

3. 仮想環境のアクティベート:
```bash
# uvコマンドを使用する場合
eval "$(uv venv)"

# または従来のvenv形式を使用する場合
source .venv/bin/activate  # macOSの場合

# 仮想環境を終了する場合
deactivate
```

4. 環境変数の設定
```bash
cp .env.template .env
# 環境変数の設定
source .env
```

5. 実行
- Web UIでの実行
```bash
cd tutorials
adk web
```
ブラウザでアクセス後、該当するチュートリアルを選択してチャットをする

- Runnerでの実行
```bash
cd tutorials/tXX_xxx_xxx
python main_xxx.py
```


## 使用方法

各チュートリアルディレクトリには個別のREADMEファイルが用意されています。チュートリアルを順番に進めることで、ADKの機能を段階的に学ぶことができます。

## 参考リンク

- [Agent Development Kit 公式ドキュメント](https://google.github.io/adk-docs/)

## 未対応範囲

- Apigeeを用いたツール: https://google.github.io/adk-docs/tools/google-cloud-tools/#apigee-api-hub-tools
- Application Integrationを用いたツール: https://google.github.io/adk-docs/tools/google-cloud-tools/#application-integration-tools