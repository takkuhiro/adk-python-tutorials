from google.adk.agents import Agent

from .sub_agents import commend_agent, strict_advice_agent

analytics_agent = Agent(
    name="analytics_agent",
    model="gemini-2.0-flash",
    description="あなたは目標分析エージェントです。",
    instruction="あなたは、分析エージェントです。ユーザーの目標から推奨される行動を分析し、ユーザーにアドバイスを行います。",
    sub_agents=[strict_advice_agent, commend_agent],
)
