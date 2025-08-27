# t13_a2a_cloud_run

A2AでCloud Run上のエージェントを連携させる

## 事前準備
- 環境構築
```
uv init
uv venv
source .venv/bin/activate
uv add google-adk # 1.12.0
```

- dice_agent
- check_prime_agent

現在のディレクトリ構成
```
(a2a-tutorial-prod) ~/develop/rs-swallow-sandbox-ai/ninomiya/a2a-tutorial-prod (ninomiya)!+$ tree
.
├── README.md
├── check_prime_agent
│     ├── __init__.py
│     └── agent.py
├── dice_agent
│     ├── __init__.py
│     └── agent.py
├── pyproject.toml
└── uv.lock
```

これら2つのエージェントを別々にCloud Runにデプロイし、疎通させてみる

## A2A実装
uv add a2a-sdk

- agent_executor.py
- __main__.py
- Dockerfile
- 環境変数に`APP_URL`を設定する。Cloud RunのデプロイURLはあらかじめ決められている。
    - `https://<name>-<project_number>.<region>.run.app`
    - project_numberは`gcloud projects list`で確認できる

- 注意点
    - 基本的に[helloworld](https://github.com/a2aproject/a2a-samples/tree/main/samples/python/agents/helloworld)と同じ実装です
    - portは8080にしています
    - gemini-2.0-flashがあるリージョンでデプロイする必要がある。例えばasia-northeast1ではダメ。

## デプロイ
```
GOOGLE_CLOUD_PROJECT=aitech-good-s15112
IMAGE_PATH=us-central1-docker.pkg.dev/
REGION=us-central1
REPOSITORY=a2a-sample
IMAGE=a2a-check-prime-agent

gcloud artifacts repositories create a2a-sample \
      --repository-format=docker \
      --location=${REGION} \
      --project=${GOOGLE_CLOUD_PROJECT} \
      --description="A2A sample agent repository"

IMAGE_PATH=${REGION}-docker.pkg.dev/${GOOGLE_CLOUD_PROJECT}/${REPOSITORY}/${IMAGE}:latest
docker build --platform linux/amd64 -t ${IMAGE_PATH} .
docker push ${IMAGE_PATH}

ENV_VARS=$(grep -v '^#' .env | grep -v '^$' | xargs | sed 's/ /,/g')
gcloud run deploy a2a-check-prime-agent \
    --image ${IMAGE_PATH} \
    --port=8080 \
    --allow-unauthenticated \
    --region=${REGION} \
    --project=${GOOGLE_CLOUD_PROJECT} \
    --memory=1Gi \
    --set-env-vars=${ENV_VARS}
```

今回は検証のために簡単に設定していますが、API keyは環境変数ではなくできればSecretsに保存してください。

ミソはAgentCardを提供するためのURLと、AgentCardに記載されるAgentの公開URLの2種類があること。

## 動作検証
- リクエストを送ってみる
```
curl -X GET https://a2a-check-prime-agent-50000000000.us-central1.run.app/.well-known/agent-card.json

# AgentCardが取得できる
# {"capabilities":{"streaming":true},"defaultInputModes":["text","text/plain"],"defaultOutputModes":["text","text/plain"],"description":"素数チェックAgent","name":"check_prime_agent","preferredTransport":"JSONRPC","protocolVersion":"0.3.0","skills":[{"description":"数値のリストを素数かどうか判定します","id":"check_prime","name":"素数判定","tags":["mathematical","computation","prime","numbers"]}],"url":"https://a2a-check-prime-agent-50000000000.us-central1.run.app","version":"1.0.0"}%
```

- python test_client.py
(この実装はわかりやすさ重視で簡略化しています)
```
--- send_message ---
{'id': '93a85af2-6127-4090-9121-5a2fe45c393d', 'jsonrpc': '2.0', 'result': {'artifacts': [{'artifactId': '8b4bd453-a598-4701-a0ad-26d55ddaccbd', 'name': 'response', 'parts': [{'kind': 'text', 'text': 'はい、7は素数です。\n'}]}], 'contextId': 'a4a0ac98-8418-4d2b-8948-4ad09ad82e46', 'history': [{'contextId': 'a4a0ac98-8418-4d2b-8948-4ad09ad82e46', 'kind': 'message', 'messageId': '68d7d617de854739ab1d70359be8d698', 'parts': [{'kind': 'text', 'text': '7は素数ですか？'}], 'role': 'user', 'taskId': '794ac6c8-df9e-42b8-a444-04da08da9c78'}, {'contextId': 'a4a0ac98-8418-4d2b-8948-4ad09ad82e46', 'kind': 'message', 'messageId': '1b0c5fb7-0ad2-49d8-81e3-f774140af757', 'parts': [{'kind': 'text', 'text': 'Processing request...'}], 'role': 'agent', 'taskId': '794ac6c8-df9e-42b8-a444-04da08da9c78'}], 'id': '794ac6c8-df9e-42b8-a444-04da08da9c78', 'kind': 'task', 'status': {'state': 'completed', 'timestamp': '2025-08-26T09:45:20.616038+00:00'}}}
--- send_message_streaming ---
{'id': 'e2c713a9-b0a3-4773-bafb-2f1cbf1135eb', 'jsonrpc': '2.0', 'result': {'contextId': '088e8ee2-64c6-494d-8b46-f10bd1a61cb0', 'history': [{'contextId': '088e8ee2-64c6-494d-8b46-f10bd1a61cb0', 'kind': 'message', 'messageId': '68d7d617de854739ab1d70359be8d698', 'parts': [{'kind': 'text', 'text': '7は素数ですか？'}], 'role': 'user', 'taskId': 'd0ee7a51-42ee-4f60-9edc-e0befd01476f'}], 'id': 'd0ee7a51-42ee-4f60-9edc-e0befd01476f', 'kind': 'task', 'status': {'state': 'submitted'}}}
{'id': 'e2c713a9-b0a3-4773-bafb-2f1cbf1135eb', 'jsonrpc': '2.0', 'result': {'contextId': '088e8ee2-64c6-494d-8b46-f10bd1a61cb0', 'final': False, 'kind': 'status-update', 'status': {'message': {'contextId': '088e8ee2-64c6-494d-8b46-f10bd1a61cb0', 'kind': 'message', 'messageId': 'e1fa2bfe-f82a-4cc7-8687-220457009355', 'parts': [{'kind': 'text', 'text': 'Processing request...'}], 'role': 'agent', 'taskId': 'd0ee7a51-42ee-4f60-9edc-e0befd01476f'}, 'state': 'working', 'timestamp': '2025-08-26T09:45:20.784097+00:00'}, 'taskId': 'd0ee7a51-42ee-4f60-9edc-e0befd01476f'}}
{'id': 'e2c713a9-b0a3-4773-bafb-2f1cbf1135eb', 'jsonrpc': '2.0', 'result': {'artifact': {'artifactId': 'b36069e2-a29a-4608-9762-4686f268f418', 'name': 'response', 'parts': [{'kind': 'text', 'text': 'はい、7は素数です。\n'}]}, 'contextId': '088e8ee2-64c6-494d-8b46-f10bd1a61cb0', 'kind': 'artifact-update', 'taskId': 'd0ee7a51-42ee-4f60-9edc-e0befd01476f'}}
{'id': 'e2c713a9-b0a3-4773-bafb-2f1cbf1135eb', 'jsonrpc': '2.0', 'result': {'contextId': '088e8ee2-64c6-494d-8b46-f10bd1a61cb0', 'final': True, 'kind': 'status-update', 'status': {'state': 'completed', 'timestamp': '2025-08-26T09:45:21.760058+00:00'}, 'taskId': 'd0ee7a51-42ee-4f60-9edc-e0befd01476f'}}
```

tool_callingで素数判定を行い、その結果を返しているのがわかります。
ここまででデプロイしたエージェントがA2Aプロトコルで接続できることがわかりました。


- dice_agentの検証
dice_agent/agent.pyを修正し、RemoteA2aAgentにする
そして、adk webでやってみる

※A2Aはリモートのエージェントがどんな処理をしているかは知らない。その証拠にRemoteA2aAgentはcheck_prime関数を実行しているが、画面にはtool callingは表示されていない。


## Cloud Runにデプロイして接続する
ローカルで実行した通り、アプリケーションを通常通りにデプロイすれば、どこからでも接続できます。
ADKではCloud Runにコマンド一発でAgent Engineをデプロイできるので、これでやってみます。
cf. https://google.github.io/adk-docs/deploy/cloud-run/#minimal-command
```
uv pip freeze > dice_agent/requirements.txt
source .env && echo $APP_URL

adk deploy cloud_run \
    --project=$GOOGLE_CLOUD_PROJECT \
    --region=$REGION \
    --service_name=a2a-dice-agent \
    --with_ui \
    ./dice_agent
```

デプロイされたのでみてみます
Service URL: https://a2a-dice-agent-50000000000.us-central1.run.app

無事実行できました

# 注意
最初、requirements.txtをagentのディレクトリに含めておらず、実行時に以下のエラーだった。
{"error": "Fail to load 'dice_agent' module. No module named 'a2a'"}
[ADKのCloud Runデプロイに関するドキュメント](https://google.github.io/adk-docs/deploy/cloud-run/#agent-sample)には以下の記載があった。
> 4. Your requirements.txt file is present in the agent directory.
気をつけたい。



## 余談
AgentCard自体に機密情報が含まれる場合は、AgentCardを公開しているサーバーへのリクエストに対して認証・認可を実装すれば良いです。
今後AgentのMarketplaceが出てくると思いますが、その場合もAgentCardだけをMarketplace上で公開しておけば、Agentが実際に稼働するサーバーはどこでも良いということになるので、便利だと思います。
個人的にはエージェント自身の循環参照にならないのか気になりました。

## 開発環境用
uv add --dev ruff black
uv run black . && uv run ruff check --fix .
