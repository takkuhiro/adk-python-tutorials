from google.adk.agents import Agent

strict_advice_agent = Agent(
    name="strict_advice_agent",
    model="gemini-2.0-flash",
    description="あなたはユーザーの目標設計に対して厳しいアドバイスを行うエージェントです。",
    instruction="あなたは、ユーザーの目標設計に対して厳しいアドバイスを行うエージェントです。ユーザーの目標設計の改善すべき点を分析し、ユーザーに厳しくアドバイスをしてあげます。",
)
