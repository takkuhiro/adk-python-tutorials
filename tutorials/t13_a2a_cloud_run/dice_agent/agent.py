import random
from google.adk import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent


APP_URL = "https://a2a-check-prime-agent-50000000000.us-central1.run.app"


def roll_die() -> int:
    """6面サイコロを振ります"""
    return random.randint(1, 6)


remote_check_prime_agent = RemoteA2aAgent(
    name="check_prime_agent",
    description="素数判定エージェント",
    agent_card=(f"{APP_URL}/.well-known/agent-card.json"),
)

root_agent = Agent(
    model="gemini-2.0-flash",
    name="dice_agent",
    description="サイコロAgent",
    instruction="ユーザーが「スタート」と言ったら、6面サイコロを振ります。出た目が素数かどうかをエージェントに判定してもらい、結果をユーザーに通知します。",
    tools=[roll_die],
    sub_agents=[remote_check_prime_agent],
)
