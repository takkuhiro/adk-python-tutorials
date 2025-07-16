import asyncio

import google.genai.types as types
from agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

session_service = InMemorySessionService()

runner = Runner(
    agent=root_agent,
    app_name="my_artifact_app",
    session_service=session_service,
)


async def main_image_input(
    query: str, image_bytes: bytes, runner: Runner, app_name: str, user_id: str, session_id: str
) -> None:
    print(f"\n>>> User Query: {query}")
    _ = await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)

    content = types.Content(
        role="user",
        parts=[
            types.Part(text=query),
            types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=image_bytes)),
            # or types.Part.from_bytes(mime_type="image/png", data=image_bytes),
        ],
    )

    final_response_text = ""

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text  # type: ignore
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break

    print(f"<<< Agent Response: {final_response_text}")


if __name__ == "__main__":
    with open("./assets/cat.jpeg", "rb") as f:
        image_bytes = f.read()
    query = "画像には何が映っていますか？"

    asyncio.run(main_image_input(query, image_bytes, runner, "my_artifact_app", "user_id", "session_id"))
