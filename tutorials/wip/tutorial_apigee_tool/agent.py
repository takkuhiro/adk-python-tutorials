from google.adk.agents import Agent

from .tools import sample_toolset_with_auth

root_agent = Agent(
    name="root_agent",
    model="gemini-2.0-flash",
    description="TavilySearchを使って質問に回答するエージェント",
    instruction="インターネットを検索して質問に回答してください。",
    tools=[sample_toolset_with_auth],
)
