from google.adk.agents import Agent
from tools import search_tool, short_story_writer_tool # NOTE: python main.py の場合はこっち
# from .tools import search_tool, short_story_writer_tool # NOTE: adk webの場合はこっち

root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="パーソナルアシスタントです。",
    instruction="あなたは、パーソナルアシスタントです。",
    tools=[search_tool, short_story_writer_tool],
)