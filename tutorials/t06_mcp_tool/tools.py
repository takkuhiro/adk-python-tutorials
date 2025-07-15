import os

from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

# もし可能であれば動的にパスを定義するのが良いです。
# また、ユーザーに絶対パスを理解させる必要があります。
# この例では、このファイルと同じディレクトリにあるbooksフォルダを想定しています。
TARGET_FOLDER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "books/")


mcp_toolset = MCPToolset(
    connection_params=StdioServerParameters(
        command="npx",
        args=[
            "-y",  # npxを自動でインストールするためのオプション
            "@modelcontextprotocol/server-filesystem",
            TARGET_FOLDER_PATH,  # npxがアクセスできるように絶対パスを指定する必要があります
        ],
    ),
    # Optional: MCPサーバーから公開するツールをフィルタリングすることができます
    # tool_filter=['list_directory', 'read_file']
)
