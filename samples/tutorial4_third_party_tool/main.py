# 以下のコードを元に修正したコードです
# cf. https://google.github.io/adk-docs/tools/third-party-tools

import asyncio
import os

from agent import root_agent
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService, Session
from google.genai import types

load_dotenv()

# Ensure TAVILY_API_KEY is set in your environment
if not os.getenv("TAVILY_API_KEY"):
    print("Warning: TAVILY_API_KEY environment variable not set.")

APP_NAME = "news_app"
USER_ID = "1234"
SESSION_ID = "session1234"


async def setup_session_and_runner() -> tuple[Session, Runner]:
    session_service = InMemorySessionService()
    session = await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    runner = Runner(agent=root_agent, app_name=APP_NAME, session_service=session_service)
    return session, runner


# Agent Interaction
async def call_agent_async(query: str) -> None:
    content = types.Content(role="user", parts=[types.Part(text=query)])
    session, runner = await setup_session_and_runner()
    events = runner.run_async(user_id=USER_ID, session_id=SESSION_ID, new_message=content)

    async for event in events:
        if event.is_final_response():
            final_response = event.content.parts[0].text  # type: ignore
            print("Agent Response: ", final_response)


if __name__ == "__main__":
    asyncio.run(call_agent_async("GOOGの株価はいくらですか？"))
