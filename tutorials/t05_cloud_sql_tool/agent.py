from google.adk.agents import Agent

from .tools import memory_tools

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="パーソナルエージェント",
    instruction="あなたはユーザーのパーソナルエージェントです。ユーザーの質問に対して、適切な回答をしてください。",
    tools=memory_tools,  # type: ignore
)
