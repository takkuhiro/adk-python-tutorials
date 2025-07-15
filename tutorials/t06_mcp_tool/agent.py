from google.adk.agents import LlmAgent

from .tools import mcp_toolset

root_agent = LlmAgent(
    model="gemini-2.0-flash",
    name="filesystem_assistant_agent",
    instruction="ユーザーがファイルを管理するためのエージェントです。ファイルを読み込んだり、書き込んだり、削除したりできます。",
    tools=[mcp_toolset],
)
