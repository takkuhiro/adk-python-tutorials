# tutorial2_agent_tool

Tool Callingを行うエージェントのサンプルです

### 実行方法
```
# venv環境に入る
source .venv/bin/activate

# Web UIから実行
# NOTE: 事前にコード内のコメントを確認してください。
# 例えば、agent.pyでは、from .tools import ...を選択する必要があります。
cd samples
adk web
# 画面からtutorial2_agent_toolを選択する

# ターミナルから実行
# NOTE: 事前にコード内のコメントを確認してください。
# 例えば、agent.pyでは、from tools import ...を選択する必要があります。
cd (root)
cp .env.template .env
# .envを自分で用意した値に設定する
source .env
cd samples/tutorial2_agent_tool
python main.py
```
