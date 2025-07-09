from google.adk.agents import Agent
from .sub_agents import analytics_agent, summary_agent


root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="パーソナルアシスタントです。",
    instruction="あなたは、パーソナルアシスタントです。",
    sub_agents=[analytics_agent, summary_agent],
)