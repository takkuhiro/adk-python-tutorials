from google.adk.agents import Agent

summary_agent = Agent(
    name="summary_agent",
    model="gemini-2.0-flash",
    description="あなたは長文に対して要約を行うエージェントです。",
    instruction="あなたは、要約エージェントです。長文が与えられた際に要約します。",
)