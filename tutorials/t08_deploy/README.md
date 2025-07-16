# t08_deploy - エージェントのデプロイ

## 概要
ADKで作成したエージェントのデプロイ方法を学ぶためのチュートリアルです。

以下へのデプロイ方法が提供されています。
- Agent Engine
- Cloud Run
- GKE

今回はAgent Engineへのデプロイを扱います

cf. 公式ドキュメント: [Deploy](https://google.github.io/adk-docs/deploy/)

## 学習内容
- `AdkApp`を使用したエージェントのパッケージング
- `agent_engines.create()`によるAgent Engineへのデプロイ

## Agent Engineへのデプロイ

### 環境変数の設定
以下の環境変数が自分のものに設定されていることを確認する
```bash
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="us-central1"
GOOGLE_CLOUD_STAGING_BUCKET="your-staging-bucket"
```

### デプロイの実行
```bash
cd tutorials/t08_deploy
python deploy_agent_engine.py
```

出力ログの例
```
~/adk-python-tutorials/tutorials/tutorial7_deploy $ python deploy_agent_engine.py
Identified the following requirements: {'pydantic': '2.11.7', 'google-cloud-aiplatform': '1.101.0', 'cloudpickle': '3.1.1'}
The following requirements are missing: {'pydantic', 'cloudpickle'}
The following requirements are appended: {'cloudpickle==3.1.1', 'pydantic==2.11.7'}
The final list of requirements: ['google-cloud-aiplatform[adk,agent_engines]', 'cloudpickle==3.1.1', 'pydantic==2.11.7']
Creating bucket adk-python-tutorials in location='us-central1'
Wrote to gs://adk-python-tutorials/agent_engine/agent_engine.pkl
Writing to gs://adk-python-tutorials/agent_engine/requirements.txt
Creating in-memory tarfile of extra_packages
Writing to gs://adk-python-tutorials/agent_engine/dependencies.tar.gz
Creating AgentEngine
Create AgentEngine backing LRO: projects/xxx/locations/us-central1/reasoningEngines/xxx/operations/xxx
View progress and logs at https://console.cloud.google.com/logs/query?project=YOUR-PROJECT

(数分後)

To use this AgentEngine in another session:
agent_engine = vertexai.agent_engines.get('projects/xxx/locations/us-central1/reasoningEngines/xxx')
Created remote agent: projects/xxx/locations/us-central1/reasoningEngines/xxx
```

デプロイには最大10分ほどかかります。完了すると以下のような形式のリソース名が表示されます：
```
projects/xxx/locations/us-central1/reasoningEngines/xxx
```


### デプロイしたエージェントの利用
```bash
# request_agent_engine.pyのAGENT_ENGINE_IDに上記のリソース名を設定
python request_agent_engine.py
```
