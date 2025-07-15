import os

import vertexai
from dotenv import load_dotenv
from vertexai import agent_engines
from vertexai.preview import reasoning_engines
from vertexai.preview.reasoning_engines import AdkApp
from agent import root_agent

load_dotenv()


app = reasoning_engines.AdkApp(agent=root_agent, enable_tracing=False)


if __name__ == "__main__":
    session = app.create_session(user_id="user_id", session_id="session_id")
    for event in app.stream_query(
        user_id="user_id",
        session_id=session.id,
        message="new yorkの天気は？",
    ):
        parts = event["content"]["parts"]
        for part in parts:
            print(part)