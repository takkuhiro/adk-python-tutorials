from google.adk.agents import Agent
from google.adk.code_executors import BuiltInCodeExecutor

# NOTE: 公式チュートリアルではここをリストにしているがエラーだった
# 以下のissueを参考に修正した
# cf. https://github.com/google/adk-python/issues/969

coding_agent = Agent(
    name="coding_agent",
    model="gemini-2.0-flash",
    description="数学などプログラミングを使って問題を解決するエージェント",
    instruction="Pythonコードを書いて実行し、結果を取得してください",
    code_executor=BuiltInCodeExecutor(),
)