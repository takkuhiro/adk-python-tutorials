import asyncio

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

agent = LlmAgent(
    name="Greeter",
    model="gemini-2.0-flash",
    instruction="あなたは、パーソナルアシスタントです。",
    output_key="last_response",  # NOTE: これにより、セッションの状態にlast_responseが保存される
)


async def main() -> None:
    app_name, user_id, session_id = "state_app", "user1", "session1"
    session_service = InMemorySessionService()
    runner = Runner(agent=agent, app_name=app_name, session_service=session_service)

    session = await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)
    print(f"初期状態: {session.state}")  # Output: {}

    # Runnerは、append_eventを呼び出し、output_keyで指定したキーを使用してstateを更新します。
    query = "こんにちは"
    user_message = Content(parts=[Part(text=query)])
    print(f"入力: {user_message.parts[0].text}")  # type: ignore[index]
    for event in runner.run(user_id=user_id, session_id=session_id, new_message=user_message):
        if event.is_final_response():
            print(f"エージェント応答: {event.content.parts[0].text}")  # type: ignore[union-attr, index]

    updated_session = await session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
    print(f"エージェント実行後の状態: {updated_session.state}")  # type: ignore[union-attr]  # Output: {'last_response': 'xxx'}


if __name__ == "__main__":
    asyncio.run(main())
