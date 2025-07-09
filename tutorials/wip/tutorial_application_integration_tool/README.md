# tutorial6_application_integration_tool

Google Cloud の Application Integration を使ったツールを利用するエージェントです

https://google.github.io/adk-docs/tools/google-cloud-tools/#application-integration-tools

### 準備
1. Google Cloud コンソールから Application Integration を選択する
2. 上記の公式サイトの通り、`ExecuteIntegration`を作成して公開する
3. Service Accountを作成して権限を付け、CredentialsをJSONファイルでダウンロードする

### 実行方法
```
# venv環境に入る
source .venv/bin/activate

# ターミナルから実行
cd (root)
cp .env.template .env
# .envを自分で用意した値に設定する
source .env
cd tutorials/tutorial5_apigee_tool
python main.py
```
