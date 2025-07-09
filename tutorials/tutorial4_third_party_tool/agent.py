from google.adk.agents import Agent
from tools import adk_tavily_tool

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="TavilySearchを使って質問に回答するエージェント",
    instruction="インターネットを検索して質問に回答してください。",
    tools=[adk_tavily_tool],
)
