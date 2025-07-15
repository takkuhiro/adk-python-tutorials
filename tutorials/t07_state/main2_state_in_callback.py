# In an agent callback or tool function
from google.adk.runners import Runner
from google.adk.agents import Agent
from google.adk.artifacts import InMemoryArtifactService # Or GcsArtifactService
from google.adk.sessions import InMemorySessionService
import google.genai.types as types
from google.adk.models import LlmRequest
from google.adk.agents.callback_context import CallbackContext # Or ToolContext
import asyncio
import uuid

def before_state_update(callback_context: CallbackContext):
    count = callback_context.state.get("user_action_count", 0)
    callback_context.state["user_action_count"] = count + 1

    # Add new state
    new_id = str(uuid.uuid4())
    callback_context.state["user:last_operation_id"] = new_id


root_agent = Agent(
    name="personal_assistant",
    model="gemini-2.0-flash",
    description="パーソナルアシスタントです。",
    instruction="あなたは、パーソナルアシスタントです。",
    before_agent_callback=before_state_update
)


async def main():
    session_service = InMemorySessionService()
    app_name, user_id, session_id = "state_app_manual", "user2", "session2"

    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id)

    runner = Runner(
        agent=root_agent,
        app_name=app_name,
        session_service=session_service
    )

    query = "こんにちは"
    user_message = types.Content(parts=[types.Part(text=query)])
    for event in runner.run(user_id=user_id, session_id=session_id, new_message=user_message):
        if event.content:
            print(event.content.parts[0].text)
            updated_session = await session_service.get_session(app_name=app_name, user_id=user_id, session_id=session_id)
            print(f"エージェント実行後の状態: {updated_session.state}")

if __name__ == "__main__":
    asyncio.run(main())