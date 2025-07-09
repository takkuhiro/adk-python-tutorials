# 以下のコードを元に修正したコードです
# cf. https://google.github.io/adk-docs/tools/built-in-tools/#code-execution

import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import coding_agent
from dotenv import load_dotenv

# NOTE: dotenvを読み込む
load_dotenv()


# NOTE: 非同期関数内でcreate_sessionを呼ぶ
session_service = InMemorySessionService()

async def setup_session_and_runner():
    session = await session_service.create_session(
        app_name="calculator", user_id="user1234", session_id="session_code_exec_async"
    )
    runner = Runner(agent=coding_agent, app_name="calculator", session_service=session_service)
    return session, runner


async def call_agent_async(query):
    print(f"\n--- Running Query: {query} ---")
    session, runner = await setup_session_and_runner()
    content = types.Content(role="user", parts=[types.Part(text=query)])
    try:
        async for event in runner.run_async(
            user_id="user1234", session_id="session_code_exec_async", new_message=content
        ):
            # --- Check for specific parts FIRST ---
            has_specific_part = False
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.executable_code:
                        # Access the actual code string via .code
                        print(
                            f"  Debug: Agent generated code:\n```python\n{part.executable_code.code}\n```"
                        )
                        has_specific_part = True
                    elif part.code_execution_result:
                        # Access outcome and output correctly
                        print(
                            f"  Debug: Code Execution Result: {part.code_execution_result.outcome} - Output:\n{part.code_execution_result.output}"
                        )
                        has_specific_part = True
                    # Also print any text parts found in any event for debugging
                    elif part.text and not part.text.isspace():
                        print(f"  Text: '{part.text.strip()}'")
                    else:
                        print(f"  Others: {part}")
                        # Do not set has_specific_part=True here, as we want the final response logic below

            # --- Check for final response AFTER specific parts ---
            # Only consider it final if it doesn't have the specific code parts we just handled
            if not has_specific_part and event.is_final_response():
                if (
                    event.content
                    and event.content.parts
                    and event.content.parts[0].text
                ):
                    final_response_text = event.content.parts[0].text.strip()
                    print(f"==> Final Agent Response: {final_response_text}")
                else:
                    print("==> Final Agent Response: [No text content in final event]")

    except Exception as e:
        print(f"ERROR during agent run: {e}")
    print("-" * 30)


# Main async function to run the examples
async def main():
    await call_agent_async("5 + 7 * 3を計算してください")
    await call_agent_async("10の階乗を計算してください")


async def dialog():
    while True:
        query = input("Enter your query: ")
        if query.lower() == "exit":
            break
        await call_agent_async(query)


if __name__ == "__main__":
    asyncio.run(main())