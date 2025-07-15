# tutorial7_deploy

ADKで作成したエージェントをデプロイします

- Agent Engine
- Cloud Run
- GKE

cf. https://google.github.io/adk-docs/deploy

### Agent Engineへのデプロイ
```
cd tutorial7_deploy
python deploy_agent_engine.py
```

すると以下の表示が出力される
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

- デプロイには最大10分ほど時間がかかる（長すぎるとエラーを疑う）
- デプロイの進捗は上記のように出力されるログエクスプローラーのリンク(https://console.cloud.google.com/logs/query?project=YOUR-PROJECT) で確認可能
- デプロイ後のremoteアクセスのためのID（上記の場合は`projects/xxx/locations/us-central1/reasoningEngines/xxx`）をメモしておき、リクエスト時に利用する

### Agent Engineの利用例
1. 上記で入手したIDを`request_agent_engine.py`のAGENT_ENGINE_IDに入力する
1. `python request_agent_engine.py`


