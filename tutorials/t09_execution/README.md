# t09_execution - エージェントの実行方法

## 概要
エージェントの実行方法の違いを学ぶためのチュートリアルです。Web UI、Runner、AdkAppなど、異なる実行方法の特徴と使い分けを実装します。

## 学習内容
- `Runner`と`InMemorySessionService`を使用した実行方法
- `AdkApp`を使用したエージェントの実行とトレーシング

## ローカル実行方法

### 1. Web UIでの実行（デバッグ用）
```bash
cd tutorials
adk web
```
起動後にブラウザで`localhost:8080`を開き、ドロップダウンメニューより`t09_execution`を選択する

### 2. Runnerによる実行
```bash
cd tutorials/t09_execution
python main_runner.py
```

### 3. AdkAppによる実行
```bash
gcloud auth application-default login
cd tutorials/t09_execution
python main_adkapp.py
```

## デプロイ済みエージェントの実行

### Agent Engineの場合
```python
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

### Cloud Run と GKE の場合
REST APIによる実行
```
# Create Session
curl -X POST \
    $APP_URL/apps/capital_agent/users/user_123/sessions/session_abc \
    -H "Content-Type: application/json" \
    -d '{"state": {"preferred_language": "English", "visit_count": 5}}'

# Run Agent
curl -X POST $APP_URL/run_sse \
    -H "Content-Type: application/json" \
    -d '{
    "app_name": "capital_agent",
    "user_id": "user_123",
    "session_id": "session_abc",
    "new_message": {
        "role": "user",
        "parts": [{
        "text": "What is the capital of Canada?"
        }]
    },
    "streaming": false
    }'
```
