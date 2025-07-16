import asyncio

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.artifacts import InMemoryArtifactService
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

load_dotenv()


def check_if_agent_should_run(callback_context: CallbackContext) -> types.Content | None:
    """
    このコールバック関数は、LLMエージェントの実行を制御するためのものです。
    エージェントの実行をスキップするかどうかを決定するために、セッションの状態をチェックします。
    セッションの状態にskip_llm_agentがTrueに設定されている場合、エージェントの実行をスキップします。
    それ以外の場合は、エージェントの実行を許可します。
    """
    agent_name = callback_context.agent_name
    invocation_id = callback_context.invocation_id
    current_state = callback_context.state.to_dict()

    print(f"[Callback] Agent名: {agent_name} (Invocation ID: {invocation_id})")
    print(f"[Callback] 現在の状態: {current_state}")

    # ここでエージェントの実行をスキップするかどうかを決定します。
    if current_state.get("skip_llm_agent", False):
        # エージェントの実行をスキップするために、Contentを返します。
        print(f"[Callback] エージェントの実行をスキップします: {agent_name}")
        return types.Content(
            parts=[types.Part(text=f"(Agent {agent_name} は、before_agent_callbackによってskippedされました)")], role="model"
        )
    else:
        # エージェントの本来の実行を許可するために、Noneを返します
        print(f"[Callback] エージェントの実行を許可します: {agent_name}")
        return None


root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="パーソナルアシスタントです。",
    instruction="あなたは、パーソナルアシスタントです。",
    before_agent_callback=check_if_agent_should_run,  # Callbackを設定します
)


async def main() -> None:
    app_name = "before_agent_demo"
    user_id = "test_user"
    session_id_run = "session_will_run"
    session_id_skip = "session_will_skip"

    session_service = InMemorySessionService()
    artifact_service = InMemoryArtifactService()
    runner = Runner(agent=root_agent, app_name=app_name, session_service=session_service, artifact_service=artifact_service)

    # 比較するために、stateを持った場合と持たなかった場合のsessionを作成する
    await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id_run,
        # stateはデフォルトのNoneなので call_back checkの中で'skip_llm_agent'はfalseになる
    )

    await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id_skip,
        state={"skip_llm_agent": True},  # call_back checkの中で'skip_llm_agent'はtrueになる
    )

    # session_serviceのlistを表示する
    print(await session_service.list_sessions(app_name=app_name, user_id=user_id))

    print("\n" + "=" * 20 + f" シナリオ 1: Running Agent on Session '{session_id_run}' (エージェントが実行される) " + "=" * 20)
    query = "好きな食べ物は？"
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id_run, new_message=types.Content(role="user", parts=[types.Part(text=query)])
    ):
        if event.is_final_response() and event.content:
            print(f"Final Output: [{event.author}] {event.content.parts[0].text.strip()}")  # type: ignore[index, union-attr]
        elif event.is_error():  # type: ignore[attr-defined]
            print(f"Error Event: {event.error_details}")  # type: ignore[attr-defined]

    print(
        "\n" + "=" * 20 + f" シナリオ 2: Running Agent on Session '{session_id_skip}' (エージェントが実行されない) " + "=" * 20
    )
    async for event in runner.run_async(
        user_id=user_id, session_id=session_id_skip, new_message=types.Content(role="user", parts=[types.Part(text=query)])
    ):
        if event.is_final_response() and event.content:
            print(f"Final Output: [{event.author}] {event.content.parts[0].text.strip()}")  # type: ignore[index, union-attr]
        elif event.is_error():  # type: ignore[attr-defined]
            print(f"Error Event: {event.error_details}")  # type: ignore[attr-defined]


if __name__ == "__main__":
    asyncio.run(main())
