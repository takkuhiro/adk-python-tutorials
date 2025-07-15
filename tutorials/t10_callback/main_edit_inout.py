import asyncio

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

load_dotenv()


def before_model_modifier(callback_context: CallbackContext, llm_request: LlmRequest) -> types.Content | None:
    """
    before_agent_callbackの中で、エージェントへの入力を編集できます
    """
    last_user_message = ""
    if llm_request.contents and llm_request.contents[-1].role == "user":
        if llm_request.contents[-1].parts:
            last_user_message = llm_request.contents[-1].parts[0].text
    # ここでメッセージを編集する
    # もしoriginal_instructionを修正したい場合は、llm_request.config.system_instructionを取得して編集する
    new_user_message = f"[入力編集] {last_user_message}"
    # llm_requestを直接編集することで入力を変更する
    llm_request.contents[-1].parts[0].text = new_user_message
    # - return None: LLMへの入力を許可する（編集して渡したい場合は上記のようにllm_requestを直接編集しておく）
    # - return Content: LLMを実行せずにContentをエージェントの応答としてそのまま出力する
    return None


def after_model_modifier(callback_context: CallbackContext, llm_response: LlmResponse) -> types.Content | None:
    """
    after_agent_callbackの中で、エージェントの出力を編集できます
    """
    last_agent_response = ""
    if llm_response.content.parts:
        last_agent_response = llm_response.content.parts[0].text
    # ここでメッセージを編集する
    new_agent_response = f"[出力編集] {last_agent_response}"

    # - return None: LLMの出力を許可する
    # - return Content: LLMの実行結果を無視してContentをエージェントの応答として出力する
    #                  （編集して渡したい場合は編集したContentをreturnする）
    new_response = LlmResponse(content=types.Content(role="agent", parts=[types.Part(text=new_agent_response)]))
    return new_response


root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="パーソナルアシスタントです。",
    instruction="あなたは、パーソナルアシスタントです。",
    before_model_callback=before_model_modifier,
    after_model_callback=after_model_modifier,
)


async def main():
    app_name = "tutorial"
    user_id = "test_user"
    session_id = "session_id"

    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name=app_name,
        session_service=session_service,
    )

    await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)

    query = "好きな食べ物は？"
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id, new_message=types.Content(role="user", parts=[types.Part(text=query)])
    ):
        print(event)


if __name__ == "__main__":
    asyncio.run(main())
