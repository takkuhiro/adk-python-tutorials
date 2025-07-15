import os

import vertexai
from dotenv import load_dotenv
from vertexai import agent_engines

load_dotenv()

vertexai.init(
    project=os.getenv("GOOGLE_CLOUD_PROJECT"),
    location=os.getenv("GOOGLE_CLOUD_LOCATION"),
    staging_bucket=os.getenv("GOOGLE_CLOUD_STAGING_BUCKET"),
)

# TODO: デプロイ時に出力されたIDに変更する
AGENT_ENGINE_ID = "REPLACE_YOUR_AGENT_ID: e.g. projects/xxx/locations/us-central1/reasoningEngines/xxx"


def list_session_ids() -> None:
    remote_app = agent_engines.get(AGENT_ENGINE_ID)

    _ = remote_app.create_session(user_id="user_id", session_id="session_id_a")
    _ = remote_app.create_session(user_id="user_id", session_id="session_id_b")
    _ = remote_app.create_session(user_id="user_id", session_id="session_id_c")

    sessions = remote_app.list_sessions(user_id="user_id")
    for session in sessions["sessions"]:
        print(session["id"])


def chat() -> None:
    print("1. Getting agent...")
    remote_app = agent_engines.get(AGENT_ENGINE_ID)

    print("2. Getting session...")
    remote_session = remote_app.create_session(user_id="user_id")

    session_id = remote_session["id"]

    print("3. Chatting...")
    while True:
        message = input("User input (Exit: break) > ")

        if message == "break":
            break

        for event in remote_app.stream_query(user_id="user_id", session_id=session_id, message=message):
            print("----- Event -----")
            print(event)
            print("-----------------")
            parts = event["content"]["parts"]
            for i, part in enumerate(parts):
                print(f"----- Part {i} -----")
                print(part)
                print("------------------")


def delete_remote_session(session_id: str) -> None:
    remote_app = agent_engines.get(AGENT_ENGINE_ID)
    remote_app.delete_session(user_id="user_id", session_id=session_id)


def delete_remote_all_sessions() -> None:
    remote_app = agent_engines.get(AGENT_ENGINE_ID)
    sessions = remote_app.list_sessions(user_id="user_id")
    for session in sessions["sessions"]:
        remote_app.delete_session(user_id="user_id", session_id=session["id"])


def delete_remote_agent() -> None:
    input(f"Are you ok deleting agent [{AGENT_ENGINE_ID}] ? > (If you ok, please enter.)")
    remote_app = agent_engines.get(AGENT_ENGINE_ID)
    remote_app.delete(force=True)


if __name__ == "__main__":
    chat()
