# Execution

ローカルでのエージェントの実行方法は3通りあります


### 実行方法
- `adk web`によるWeb UIでの実行（主にデバッグ）
(tutorial0で実行した方法です)

- RunnerとSession Makerによる実行
```
cd tutorial12_execution
python main_runner.py
```

- AdkAppによる実行
```
gcloud auth application-default login
cd tutorial12_execution
python main_adkapp.py
```

デプロイされたエージェントの実行方法は2通りあります

- Agent Engineの場合: AdkAppによる実行
```
from vertexai import agent_engines

agent_id = "デプロイ時に取得したAgentのID"
remote_app = agent_engines.get(agent_id)

_ = remote_app.create_session(user_id="user_id", session_id="session_id_a")

for event in remote_app.stream_query(
    user_id="user_id",
    session_id=session_id,
    message=message
):
    parts = event["content"]["parts"]
    for part in parts:
        print(part)
```

- Cloud Runの場合: REST APIによる実行
