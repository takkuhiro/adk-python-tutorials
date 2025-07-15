import asyncio

import google.genai.types as types
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext  # Or ToolContext
from google.adk.artifacts import InMemoryArtifactService  # Or GcsArtifactService
from google.adk.models import LlmRequest
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService


async def save_and_load_image(callback_context: CallbackContext, llm_request: LlmRequest) -> None:
    last_user_message = ""
    if llm_request.contents and llm_request.contents[-1].role == "user":
        if llm_request.contents[-1].parts:
            last_user_message = llm_request.contents[-1].parts[0].text
    print(f"[Callback] Agentに入力されるメッセージ: {last_user_message}")

    # 画像を保存
    image_bytes = llm_request.contents[-1].parts[1].inline_data.data
    image_artifact = types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=image_bytes))
    filename = "image.jpeg"

    try:
        version = await callback_context.save_artifact(filename=filename, artifact=image_artifact)
        print(f"Successfully saved Python artifact '{filename}' as version {version}.")
    except ValueError as e:
        print(f"Error saving Python artifact: {e}. Is ArtifactService configured in Runner?")
    except Exception as e:
        print(f"An unexpected error occurred during Python artifact save: {e}")

    # 画像を読み込み
    filename = "image.jpeg"
    try:
        image_artifact = await callback_context.load_artifact(filename=filename)
        if image_artifact and image_artifact.inline_data:
            print(f"Successfully loaded latest Python artifact '{filename}'.")
            print(f"MIME Type: {image_artifact.inline_data.mime_type}")
            image_bytes = image_artifact.inline_data.data
            print(f"Image size: {len(image_bytes)} bytes.")
        else:
            print(f"Python artifact '{filename}' not found.")
    except ValueError as e:
        print(f"Error loading Python artifact: {e}. Is ArtifactService configured?")
    except Exception as e:
        print(f"An unexpected error occurred during Python artifact load: {e}")

    # 入力に渡す
    new_content = types.Content(
        role="user",
        parts=[
            types.Part(text=last_user_message),
            types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=image_bytes)),
        ],
    )
    llm_request.contents.append(new_content)

    return None


async def main() -> None:
    root_agent = Agent(
        name="personal_assistant",
        model="gemini-2.0-flash",
        description="パーソナルアシスタントです。",
        instruction="あなたは、パーソナルアシスタントです。",
        before_model_callback=save_and_load_image,  # NOTE: before_agent_callbackではなく、before_model_callbackを使用する
    )

    artifact_service = InMemoryArtifactService()
    session_service = InMemorySessionService()

    runner = Runner(
        agent=root_agent,
        app_name="my_artifact_app",
        session_service=session_service,
        artifact_service=artifact_service,
    )

    image_file_name = "cat.jpeg"
    with open(f"./assets/{image_file_name}", "rb") as f:
        image_bytes = f.read()

    query = "画像には何が映っていますか？"
    app_name = "my_artifact_app"
    user_id = "user_id"
    session_id = "session_id"

    _ = await session_service.create_session(app_name=app_name, user_id=user_id, session_id=session_id)

    content = types.Content(
        role="user",
        parts=[
            types.Part(text=query),
            types.Part(inline_data=types.Blob(mime_type="image/jpeg", data=image_bytes)),
        ],
    )
    final_response_text = ""
    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break

    print(f"<<< Agent Response: {final_response_text}")


if __name__ == "__main__":
    asyncio.run(main())
