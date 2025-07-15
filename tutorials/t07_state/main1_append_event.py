from google.adk.sessions import InMemorySessionService
from google.adk.events import Event, EventActions
import asyncio
import time

async def main():
    session_service = InMemorySessionService()
    app_name, user_id, session_id = "state_app_manual", "user2", "session2"

    # 初期状態を設定してsession作成
    session = await session_service.create_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id,
        state={"user:login_count": 0, "task_status": "idle"}
    )
    print(f"初期状態: {session.state}") # Output: 初期状態: {'user:login_count': 0, 'task_status': 'idle'}

    # 状態変更を定義
    current_time = time.time()
    state_changes = {
        "task_status": "active",
        "user:login_count": session.state.get("user:login_count", 0) + 1,
        "user:last_login_ts": current_time,
        "temp:validation_needed": True
    }

    # NOTE: プレフィックスに応じて変化
    # - `user:`で始まる場合、そのユーザーのすべてのセッションで共有される
    # - `app:`で始まる場合、そのアプリケーションのすべてのユーザーとセッションで共有される
    # - `temp:`で始まる場合、一次的な利用後に必ず破棄される
    # - それ以外の場合、セッションの状態に保存される

    # 状態を更新
    actions_with_update = EventActions(state_delta=state_changes)
    system_event = Event(
        invocation_id="inv_login_update",
        author="system", # Or 'agent', 'tool' etc.
        actions=actions_with_update,
        timestamp=current_time
    )
    await session_service.append_event(session, system_event)

    # 状態が更新されたことを確認
    updated_session = await session_service.get_session(
        app_name=app_name,
        user_id=user_id,
        session_id=session_id
    )
    print(f"状態更新後: {updated_session.state}")
    # Output: 状態更新後: {'user:login_count': 1, 'task_status': 'active', 'user:last_login_ts': 1752225547.1642141}
    # NOTE: 'temp:validation_needed' は状態更新したが存在しない。これは一次的な利用後にすぐ破棄されるため。Callback時に有用。

if __name__ == "__main__":
    asyncio.run(main())