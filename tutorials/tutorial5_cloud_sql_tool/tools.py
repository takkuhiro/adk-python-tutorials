import os

from dotenv import load_dotenv
from toolbox_core import ToolboxSyncClient

load_dotenv()

MCP_TOOLBOX_URL = os.getenv("MCP_TOOLBOX_URL", "")
toolbox = ToolboxSyncClient(MCP_TOOLBOX_URL)

# 1つずつ読み込む場合
# memory_tools = toolbox.load_tool("search-memory")

# まとめて読み込む場合
memory_tools = toolbox.load_toolset("memory-toolset")
