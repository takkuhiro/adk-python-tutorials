import asyncio

from agent import root_agent  # NOTE: python main.py の場合はこっち
# from .agent import root_agent # NOTE: adk webの場合はこっち
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session
from google.genai import types


load_dotenv()

async def setup_session_and_runner() -> tuple[Session, Runner]:
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name="personal_assistant", user_id="user1234", session_id="1234")
    runner = Runner(agent=root_agent, app_name="personal_assistant", session_service=session_service)
    return session, runner


async def call_agent_async(query: str) -> None:
    content = types.Content(role="user", parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner()
    events = runner.run_async(user_id="user1234", session_id="1234", new_message=content)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text  # type: ignore
            print("Agent Response: ", final_response)


if __name__ == "__main__":
    asyncio.run(call_agent_async("世界で２番目に高い山は何か、検索してください"))
