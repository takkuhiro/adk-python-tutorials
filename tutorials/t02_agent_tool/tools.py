import time
from collections.abc import Callable
from typing import Any

from google.adk.agents import Agent
from google.adk.tools import LongRunningFunctionTool, google_search
from google.adk.tools.agent_tool import AgentTool

# --- Agent as a Tool ---
short_story_writer = Agent(
    name="short_story_writer",
    model="gemini-2.0-flash",
    description="短編小説を書くエージェント",
    instruction="100文字以内で小説を書いてください。",
)
short_story_writer_tool = AgentTool(agent=short_story_writer)


# --- Agent as a Tool with Built in Tool ---
# NOTE:
# 現在、ルートエージェントまたは単一エージェントごとに、1つの組み込みツールのみがサポートされています。
# 同じエージェント内で他のツールをいかなる種類も使用することはできません。
# 他のツールと併用したい場合はAgentToolを使用してください。
search_agent = Agent(
    name="search_agent",
    model="gemini-2.0-flash",
    description="Google検索エージェント",
    instruction="Google検索を使ってユーザーの質問に回答してください。",
    tools=[google_search],
)
search_tool = AgentTool(agent=search_agent)  # こっちを使う


# --- LongRunningFunctionTool ---
def claim_expense(purpose: str, amount: float) -> dict[str, Any]:
    """経費申請を行う"""
    # import requests
    # try:
    #     response = requests.post(
    #         'https://api.example.com/approve',
    #         json={'purpose': purpose, 'amount': amount}
    #     )
    # except Exception as e:
    #     return {'status': 'error', 'purpose' : purpose, 'amount': amount, 'ticket-id': 'approval-ticket-1'}
    # body = response.json()
    # ticket_id, approver = body['ticket-id'], body['approver']
    # if response.status_code == 200:
    #     return {'status': 'success', 'approver': approver, 'purpose' : purpose, 'amount': amount, 'ticket-id': ticket_id}
    # else:
    #     return {'status': 'error', 'purpose' : purpose, 'amount': amount, 'ticket-id': ticket_id}

    # Demo
    for i in range(10):
        print(f"Processing... {i}")
        time.sleep(1)
    return {
        "status": "success",
        "approver": "田中太郎",
        "purpose": purpose,
        "amount": amount,
        "ticket-id": "approval-ticket-1",
    }


claim_expense_tool = LongRunningFunctionTool(func=claim_expense)


# --- Not Working Tool ---
# NOTE: setはJSON Serializationできないので、エラーが出力される
def claim_expense_not_working1(purpose: str, amount: float) -> dict[str, Any]:
    """経費申請を作成する"""
    approved_set = {"ticket-id-1", "ticket-id-2", "ticket-id-3"}
    result = {
        "status": "success",
        "approved_set": approved_set,
        "purpose": purpose,
        "amount": amount,
    }
    return result


# NOTE: 関数はJSON Serializationできないので、エラーが出力される
def claim_expense_not_working2(purpose: str, amount: float) -> Callable[[], str]:
    """経費申請を作成する"""

    def _approve() -> str:
        return "OK"

    return _approve
