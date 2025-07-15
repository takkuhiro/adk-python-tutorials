import asyncio
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService, Session
from google.adk.memory import InMemoryMemoryService # Import MemoryService
from google.adk.runners import Runner
from google.adk.tools import load_memory # Tool to query memory
from google.genai.types import Content, Part

# --- Constants ---
APP_NAME = "memory_example_app"
USER_ID = "mem_user"
MODEL = "gemini-2.0-flash" # Use a valid model

session_service = InMemorySessionService()
memory_service = InMemoryMemoryService()

from google.adk.agents import Agent
from google.genai import types

class MyAgent(Agent):
    def __init__(self, memory_service: InMemoryMemoryService, **kwargs):
        super().__init__(**kwargs)
        self.memory_service = memory_service

    async def search_memory(self, query: str) -> str:
        return await self.memory_service.search_memory(query)

    async def run(self, request: types.Content, **kwargs) -> types.Content:
        # Get the user's latest message
        user_query = request.parts[0].text

        # Search the memory for context related to the user's query
        search_result = await self.search_memory(query=user_query)

        # Create a prompt that includes the retrieved memories
        prompt = f"Based on my memory, here's what I recall about your query: {search_result.memories}\n\nNow, please respond to: {user_query}"

        # Call the LLM with the enhanced prompt
        return await self.llm.generate_content_async(prompt)

# --- Agent Definitions ---
# Agent 1: Simple agent to capture information
info_capture_agent = LlmAgent(
    model=MODEL,
    name="InfoCaptureAgent",
    instruction="Acknowledge the user's statement.",
    # output_key="captured_info" # Could optionally save to state too
)

# # Agent 2: Agent that can use memory
# memory_recall_agent = LlmAgent(
#     model=MODEL,
#     name="MemoryRecallAgent",
#     instruction="Answer the user's question. Use the 'load_memory' tool "
#                 "if the answer might be in past conversations.",
#     tools=[load_memory] # Give the agent the tool
# )
memory_recall_agent = MyAgent(
    model=MODEL,
    name="MemoryRecallAgent",
    memory_service=memory_service
)


runner_1 = Runner(
    agent=info_capture_agent, # まずはinfo_capture_agentを実行
    app_name=APP_NAME,
    session_service=session_service,
    memory_service=memory_service # Memory Service
)

runner_2 = Runner(
    agent=memory_recall_agent, # 次にmemory_recall_agentを実行
    app_name=APP_NAME,
    session_service=session_service,
    memory_service=memory_service # Memory Service
)
# --- Scenario ---

async def run1_info_capture_agent():
    # 1. セッションを作成
    session1_id = "session_info"
    session1 = await runner_1.session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=session1_id)
    user_input1 = Content(parts=[Part(text="お気に入りのプロジェクトはProject Alphaです")], role="user")

    # 2. エージェント実行
    final_response_text = ""
    async for event in runner_1.run_async(user_id=USER_ID, session_id=session1_id, new_message=user_input1):
        if event.is_final_response() and event.content and event.content.parts:
            final_response_text = event.content.parts[0].text
    print(f"Agent 1 応答: {final_response_text}")

    # 3. セッションをメモリに追加
    completed_session1 = await runner_1.session_service.get_session(app_name=APP_NAME, user_id=USER_ID, session_id=session1_id)
    # memory_service = await memory_service.add_session_to_memory(completed_session1)
    print("セッションがメモリに追加されました。")

async def run2_memory_recall_agent():
    session2_id = "session_memory"
    session2 = await runner_2.session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=session2_id)
    user_input2 = Content(parts=[Part(text="以前お話しした、お気に入りのプロジェクトを思い出してください")], role="user")

    async for event in runner_2.run_async(user_id=USER_ID, session_id=session2_id, new_message=user_input2):
        print(event)
        if event.is_final_response() and event.content and event.content.parts:
            final_response_text = event.content.parts[0].text
    print(f"Agent 2 応答: {final_response_text}")

if __name__ == "__main__":
    asyncio.run(run1_info_capture_agent())
    asyncio.run(run2_memory_recall_agent())